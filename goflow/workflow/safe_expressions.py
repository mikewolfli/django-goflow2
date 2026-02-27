#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import ast
import json
import re
from django.conf import settings


_TIMEOUT_PREFIX_RE = re.compile(r"^\s*timeout\s*:\s*(\d+)\s*([a-zA-Z]+)\s*$")
_LEGACY_TIMEOUT_RE = re.compile(
    r"^\s*workitem\.time_?out\(\s*(\d+)\s*(?:,\s*unit\s*=\s*['\"]([a-zA-Z]+)['\"])??\s*\)\s*$"
)
_UNIT_ALIASES = {
    'weeks': 'w',
    'week': 'w',
    'w': 'w',
    'days': 'd',
    'day': 'd',
    'd': 'd',
    'hours': 'h',
    'hour': 'h',
    'h': 'h',
    'minutes': 'm',
    'minute': 'm',
    'min': 'm',
    'm': 'm',
    'seconds': 's',
    'second': 's',
    'sec': 's',
    's': 's',
}


def parse_params_mapping(raw_value):
    if raw_value is None:
        return {}
    if isinstance(raw_value, dict):
        return raw_value

    text = str(raw_value).strip()
    if not text:
        return {}

    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    try:
        data = ast.literal_eval(text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    return {}


def is_timeout_condition(condition):
    if not condition:
        return False
    text = str(condition).strip()
    if not text:
        return False
    return bool(_TIMEOUT_PREFIX_RE.match(text) or _LEGACY_TIMEOUT_RE.match(text))


def _parse_timeout(condition):
    text = str(condition).strip()
    match = _TIMEOUT_PREFIX_RE.match(text)
    if match:
        return int(match.group(1)), match.group(2)
    legacy_match = _LEGACY_TIMEOUT_RE.match(text)
    if legacy_match:
        delay = int(legacy_match.group(1))
        unit = legacy_match.group(2) or 'days'
        return delay, unit
    return None


def normalize_condition_text(condition):
    if condition is None:
        return ''
    text = str(condition).strip()
    if not text:
        return ''

    timeout = _parse_timeout(text)
    if timeout:
        delay, unit = timeout
        compact = _UNIT_ALIASES.get(str(unit).lower(), str(unit).lower())
        return 'timeout:%s%s' % (delay, compact)

    lowered = text.lower()
    if lowered in ('true', 'false'):
        return lowered

    if lowered.startswith(('eq:', 'ne:', 'in:', 'notin:', 'timeout:')):
        return text

    expression_tokens = ('==', '!=', ' in ', ' not in ', ' and ', ' or ', '(', ')', '>', '<')
    if any(token in text for token in expression_tokens):
        return text

    return 'eq:%s' % text


def _condition_strategy():
    strategy = getattr(settings, 'GOFLOW_CONDITION_STRATEGY', 'compatible')
    strategy = str(strategy).strip().lower()
    if strategy not in ('strict', 'compatible'):
        return 'compatible'
    return strategy


class _SafeExpressionEvaluator(ast.NodeVisitor):
    def __init__(self, context):
        self.context = context

    def evaluate(self, expression_text):
        tree = ast.parse(expression_text, mode='eval')
        return self.visit(tree)

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_Constant(self, node):
        return node.value

    def visit_Name(self, node):
        if node.id in self.context:
            return self.context[node.id]
        if node.id == 'True':
            return True
        if node.id == 'False':
            return False
        if node.id == 'None':
            return None
        raise ValueError('name not allowed: %s' % node.id)

    def visit_List(self, node):
        return [self.visit(item) for item in node.elts]

    def visit_Tuple(self, node):
        return tuple(self.visit(item) for item in node.elts)

    def visit_Dict(self, node):
        return {
            self.visit(key): self.visit(value)
            for key, value in zip(node.keys, node.values)
        }

    def visit_BoolOp(self, node):
        values = [self.visit(value) for value in node.values]
        if isinstance(node.op, ast.And):
            result = True
            for value in values:
                result = result and bool(value)
            return result
        if isinstance(node.op, ast.Or):
            result = False
            for value in values:
                result = result or bool(value)
            return result
        raise ValueError('bool operator not allowed')

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.Not):
            return not bool(operand)
        raise ValueError('unary operator not allowed')

    def visit_Compare(self, node):
        left = self.visit(node.left)
        comparisons = zip(node.ops, node.comparators)
        current_left = left
        for operator, comparator_node in comparisons:
            right = self.visit(comparator_node)
            if isinstance(operator, ast.Eq):
                ok = current_left == right
            elif isinstance(operator, ast.NotEq):
                ok = current_left != right
            elif isinstance(operator, ast.In):
                ok = current_left in right
            elif isinstance(operator, ast.NotIn):
                ok = current_left not in right
            elif isinstance(operator, ast.Gt):
                ok = current_left > right
            elif isinstance(operator, ast.GtE):
                ok = current_left >= right
            elif isinstance(operator, ast.Lt):
                ok = current_left < right
            elif isinstance(operator, ast.LtE):
                ok = current_left <= right
            else:
                raise ValueError('compare operator not allowed')
            if not ok:
                return False
            current_left = right
        return True

    def visit_Attribute(self, node):
        value = self.visit(node.value)
        attribute_name = node.attr
        if attribute_name.startswith('_'):
            raise ValueError('private attribute not allowed')
        attribute_value = getattr(value, attribute_name)
        if callable(attribute_value):
            return attribute_value
        return attribute_value

    def visit_Call(self, node):
        func = self.visit(node.func)
        if not callable(func):
            raise ValueError('call target is not callable')

        owner_name = None
        method_name = None
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            owner_name = node.func.value.id
            method_name = node.func.attr

        if owner_name == 'workitem' and method_name in ('time_out',):
            args = [self.visit(arg) for arg in node.args]
            kwargs = {kw.arg: self.visit(kw.value) for kw in node.keywords}
            return func(*args, **kwargs)

        raise ValueError('function call not allowed')

    def generic_visit(self, node):
        raise ValueError('expression node not allowed: %s' % node.__class__.__name__)


def _evaluate_simple_keyword(text, instance):
    lowered = text.lower()
    if lowered in ('true', 'yes', '1'):
        return True
    if lowered in ('false', 'no', '0'):
        return False

    if text.startswith('eq:'):
        return (instance is not None) and (instance.condition == text[3:].strip())
    if text.startswith('ne:'):
        return (instance is not None) and (instance.condition != text[3:].strip())
    if text.startswith('in:'):
        if instance is None:
            return False
        values = [value.strip() for value in text[3:].split(',') if value.strip()]
        return instance.condition in values
    if text.startswith('notin:'):
        if instance is None:
            return False
        values = [value.strip() for value in text[6:].split(',') if value.strip()]
        return instance.condition not in values
    return None


def evaluate_condition_expression(condition, workitem=None, instance=None, wfobject=None):
    if not condition:
        return True

    text = str(condition).strip()
    if not text:
        return True

    timeout = _parse_timeout(text)
    if timeout and workitem is not None:
        delay, unit = timeout
        return workitem.time_out(delay, unit=unit)

    simple_result = _evaluate_simple_keyword(text, instance)
    if simple_result is not None:
        return simple_result

    context = {
        'instance': instance,
        'workitem': workitem,
        'wfobject': wfobject,
    }

    evaluator = _SafeExpressionEvaluator(context)
    try:
        result = evaluator.evaluate(text)
    except Exception:
        strategy = _condition_strategy()
        if strategy == 'strict':
            return False
        return (instance is not None) and (instance.condition == text)

    if isinstance(result, bool):
        return result
    if isinstance(result, str) and instance is not None:
        return instance.condition == result
    return bool(result)
