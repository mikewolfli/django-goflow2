import re
from datetime import timedelta


_DURATION_RE = re.compile(r"^(?P<value>\d+)(?P<unit>[smhdw])$")


def parse_duration(value):
    if value is None:
        return None
    if isinstance(value, timedelta):
        return value
    if isinstance(value, (int, float)):
        return timedelta(seconds=int(value))
    text = str(value).strip().lower()
    if not text:
        return None

    match = _DURATION_RE.match(text)
    if not match:
        raise ValueError('invalid duration format: %s' % value)

    amount = int(match.group('value'))
    unit = match.group('unit')
    if unit == 's':
        return timedelta(seconds=amount)
    if unit == 'm':
        return timedelta(minutes=amount)
    if unit == 'h':
        return timedelta(hours=amount)
    if unit == 'd':
        return timedelta(days=amount)
    if unit == 'w':
        return timedelta(weeks=amount)
    raise ValueError('unsupported duration unit: %s' % unit)
