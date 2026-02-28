from pathlib import Path


TARGETS = {
    Path('goflow/locale/ru/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Мониторинг workflow',
        'Instances': 'Экземпляры',
        'Total': 'Всего',
        'Running': 'Выполняется',
        'Active': 'Активно',
        'Complete': 'Завершено',
        'Workitems': 'Рабочие элементы',
        'Inactive': 'Неактивно',
        'Blocked': 'Заблокировано',
        'Fallout': 'Сбой',
        'Warned': 'Предупреждено',
        'Breached': 'Нарушено',
        'Top Processes': 'Топ процессов',
        'Process': 'Процесс',
        'No data': 'Нет данных',
        'Recent Audit Events': 'Последние события аудита',
        'Time': 'Время',
        'Action': 'Действие',
        'Actor': 'Исполнитель',
        'No events': 'Нет событий',
        'Recent Fallout': 'Последние сбои',
        'Workitem': 'Рабочий элемент',
        'Activity': 'Активность',
        'Updated': 'Обновлено',
        'No fallout': 'Нет сбоев',
        'Sample Task': 'Пример задачи',
        'Request #123': 'Заявка #123',
        'Urgent': 'Срочно',
        'Needs review': 'Требуется проверка',
        'Comment': 'Комментарий',
        'Approve': 'Одобрить',
        'Reject': 'Отклонить',
        'process %s disabled.': 'процесс %s отключен.',
        'completion page.': 'страница завершения.',
        'Welcome,': 'Добро пожаловать,',
        'Change password': 'Изменить пароль',
        'Log out': 'Выйти',
        'Log in': 'Войти',
        'Workflow Designer': 'Конструктор workflow',
        'Status': 'Статус',
        'idle': 'ожидание',
        'Process Settings': 'Настройки процесса',
        'Begin Activity': 'Начальная активность',
        'End Activity': 'Конечная активность',
        'Save': 'Сохранить',
        'Reload': 'Обновить',
        'Undo': 'Отменить',
        'Redo': 'Повторить',
        'Delete Selected': 'Удалить выбранное',
        'Shortcuts': 'Горячие клавиши',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S Сохранить',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R Обновить',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z Отменить',
        'Del Delete': 'Del Удалить',
        'Activities': 'Активности',
        'Title': 'Название',
        'Start': 'Старт',
        'Kind': 'Тип',
        'Node Type': 'Тип узла',
        'Form Template': 'Шаблон формы',
        'Form Class': 'Класс формы',
        'Autostart': 'Автозапуск',
        'Autofinish': 'Автозавершение',
        'Add Activity': 'Добавить активность',
        'Transitions': 'Переходы',
        'From': 'Откуда',
        'To': 'Куда',
        'Name': 'Имя',
        'approve': 'одобрить',
        'Condition': 'Условие',
        'Add Transition': 'Добавить переход',
        'Canvas': 'Схема',
        'Keyboard Shortcuts': 'Сочетания клавиш',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: Сохранить',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: Обновить',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: Отменить',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: Повторить',
        'Delete/Backspace: Delete selected': 'Delete/Backspace: удалить выбранное',
        'Double-click node: Rename': 'Двойной клик по узлу: переименовать',
        'Click edge: Edit label/condition': 'Клик по ребру: изменить метку/условие',
        'Close': 'Закрыть',
        'Validation errors': 'Ошибки валидации',
        'Rename activity': 'Переименовать активность',
        'Transition condition or name': 'Условие или имя перехода',
        'loading': 'загрузка',
        'Reloaded': 'Обновлено',
        'ready': 'готово',
        'Reload failed': 'Ошибка обновления',
        'error': 'ошибка',
        'saving': 'сохранение',
        'Save failed': 'Ошибка сохранения',
        'validation error': 'ошибка валидации',
        'Saved': 'Сохранено',
        'saved': 'сохранено',
        'user is not active': 'пользователь не активен',
        'authentication failed': 'ошибка аутентификации',
        'user page.': 'страница пользователя.',
        'Forbidden': 'Доступ запрещён',
        'At least one activity is required.': 'Требуется как минимум одна активность.',
        'Untitled': 'Без названия',
        'Every activity must have a title.': 'Каждая активность должна иметь название.',
        'Activity titles must be 100 characters or fewer.': 'Название активности должно содержать не более 100 символов.',
        'Activity kind must be one of: %(choices)s.': 'Тип активности должен быть одним из: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'Тип узла активности должен быть одним из: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Активность "%(title)s": узлы gateway должны использовать kind=dummy.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Активность "%(title)s": для узлов %(node_type)s рекомендуется включить autostart.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Активность "%(title)s": для узлов script рекомендуется включить autofinish.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Активность "%(title)s": узлы notification не должны использовать form_class.',
        'Activity titles must be unique.': 'Названия активностей должны быть уникальными.',
        'Begin activity must exist in the workflow.': 'Начальная активность должна существовать в workflow.',
        'End activity must exist in the workflow.': 'Конечная активность должна существовать в workflow.',
        'Begin activity is required.': 'Начальная активность обязательна.',
        'End activity is required.': 'Конечная активность обязательна.',
        'Begin and End activities must be different.': 'Начальная и конечная активности должны отличаться.',
        'At least one transition is required.': 'Требуется как минимум один переход.',
        'Transitions must connect valid activities.': 'Переходы должны соединять корректные активности.',
        'Transitions cannot point to the same activity.': 'Переходы не могут указывать на одну и ту же активность.',
        'Transitions must have a name or condition.': 'Переходы должны иметь имя или условие.',
        'Duplicate transitions are not allowed.': 'Дублирующиеся переходы не допускаются.',
        'All activities must be connected by at least one transition.': 'Все активности должны быть связаны хотя бы одним переходом.',
        'Begin activity cannot have incoming transitions.': 'У начальной активности не может быть входящих переходов.',
        'Begin activity must have at least one outgoing transition.': 'У начальной активности должен быть хотя бы один исходящий переход.',
        'End activity cannot have outgoing transitions.': 'У конечной активности не может быть исходящих переходов.',
        'End activity must have at least one incoming transition.': 'У конечной активности должен быть хотя бы один входящий переход.',
        'Only one default (empty) transition is allowed per activity.': 'Для каждой активности допускается только один переход по умолчанию (пустой).',
        'All activities must be reachable from Begin.': 'Все активности должны быть достижимы от Begin.',
    },
    Path('leavedemo/locale/ru/LC_MESSAGES/django.po'): {
        'English': 'Английский',
        'French': 'Французский',
        'Simplified Chinese': 'Китайский (упрощённый)',
        'Traditional Chinese': 'Китайский (традиционный)',
        'Japanese': 'Японский',
        'Korean': 'Корейский',
        'German': 'Немецкий',
        'Spanish': 'Испанский',
        'Italian': 'Итальянский',
        'Portuguese': 'Португальский',
        'Russian': 'Русский',
        'Log in': 'Войти',
    },
    Path('sampleproject/locale/ru/LC_MESSAGES/django.po'): {
        'English': 'Английский',
        'French': 'Французский',
        'Simplified Chinese': 'Китайский (упрощённый)',
        'Traditional Chinese': 'Китайский (традиционный)',
        'Japanese': 'Японский',
        'Korean': 'Корейский',
        'German': 'Немецкий',
        'Spanish': 'Испанский',
        'Italian': 'Итальянский',
        'Portuguese': 'Португальский',
        'Russian': 'Русский',
    },
}


def unquote(value: str) -> str:
    value = value.strip()
    if not (value.startswith('"') and value.endswith('"')):
        return ''
    body = value[1:-1]
    return bytes(body, 'utf-8').decode('unicode_escape')


def quote(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'


def apply_translations(path: Path, mapping: dict[str, str]) -> int:
    lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
    changed = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith('msgid ""'):
            i += 1
            continue
        if not lines[i].startswith('msgid '):
            i += 1
            continue

        msgid = unquote(lines[i][6:])
        j = i + 1
        while j < len(lines) and lines[j].startswith('"'):
            msgid += unquote(lines[j])
            j += 1

        if msgid in mapping and j < len(lines) and lines[j].startswith('msgstr '):
            start = j
            j += 1
            while j < len(lines) and lines[j].startswith('"'):
                j += 1
            new_line = 'msgstr ' + quote(mapping[msgid])
            if lines[start:j] != [new_line]:
                lines[start:j] = [new_line]
                changed += 1
                j = start + 1

        i = j

    if changed:
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return changed


def main() -> None:
    total = 0
    for po_path, mapping in TARGETS.items():
        if not po_path.exists():
            continue
        updated = apply_translations(po_path, mapping)
        if updated:
            print(f'{po_path}: {updated}')
            total += updated
    print(f'total updated: {total}')


if __name__ == '__main__':
    main()