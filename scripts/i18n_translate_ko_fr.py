from pathlib import Path


TARGETS = {
    Path('goflow/locale/ko/LC_MESSAGES/django.po'): {
        'Workflow Monitor': '워크플로 모니터',
        'Instances': '인스턴스',
        'Total': '전체',
        'Running': '실행 중',
        'Active': '활성',
        'Complete': '완료',
        'Workitems': '작업 항목',
        'Inactive': '비활성',
        'Blocked': '차단됨',
        'Fallout': '오류',
        'Warned': '경고됨',
        'Breached': '위반됨',
        'Top Processes': '상위 프로세스',
        'Process': '프로세스',
        'No data': '데이터 없음',
        'Recent Audit Events': '최근 감사 이벤트',
        'Time': '시간',
        'Action': '작업',
        'Actor': '수행자',
        'No events': '이벤트 없음',
        'Recent Fallout': '최근 오류',
        'Workitem': '작업 항목',
        'Activity': '액티비티',
        'Updated': '업데이트됨',
        'No fallout': '오류 없음',
        'Sample Task': '샘플 작업',
        'Request #123': '요청 #123',
        'Urgent': '긴급',
        'Needs review': '검토 필요',
        'Comment': '코멘트',
        'Approve': '승인',
        'Reject': '반려',
        'process %s disabled.': '프로세스 %s 가 비활성화되었습니다.',
        'completion page.': '완료 페이지.',
        'Welcome,': '환영합니다,',
        'Change password': '비밀번호 변경',
        'Log out': '로그아웃',
        'Log in': '로그인',
        'Workflow Designer': '워크플로 디자이너',
        'Status': '상태',
        'idle': '대기',
        'Process Settings': '프로세스 설정',
        'Begin Activity': '시작 액티비티',
        'End Activity': '종료 액티비티',
        'Save': '저장',
        'Reload': '새로고침',
        'Undo': '실행 취소',
        'Redo': '다시 실행',
        'Delete Selected': '선택 삭제',
        'Shortcuts': '단축키',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S 저장',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R 새로고침',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z 실행 취소',
        'Del Delete': 'Del 삭제',
        'Activities': '액티비티',
        'Title': '제목',
        'Start': '시작',
        'Kind': '종류',
        'Node Type': '노드 유형',
        'Form Template': '폼 템플릿',
        'Form Class': '폼 클래스',
        'Autostart': '자동 시작',
        'Autofinish': '자동 완료',
        'Add Activity': '액티비티 추가',
        'Transitions': '전이',
        'From': '시작',
        'To': '도착',
        'Name': '이름',
        'approve': '승인',
        'Condition': '조건',
        'Add Transition': '전이 추가',
        'Canvas': '캔버스',
        'Keyboard Shortcuts': '키보드 단축키',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: 저장',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: 새로고침',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: 실행 취소',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: 다시 실행',
        'Delete/Backspace: Delete selected': 'Delete/Backspace: 선택 삭제',
        'Double-click node: Rename': '노드를 더블클릭: 이름 변경',
        'Click edge: Edit label/condition': '엣지 클릭: 라벨/조건 편집',
        'Close': '닫기',
        'Validation errors': '검증 오류',
        'Rename activity': '액티비티 이름 변경',
        'Transition condition or name': '전이 조건 또는 이름',
        'loading': '로딩 중',
        'Reloaded': '새로고침 완료',
        'ready': '준비됨',
        'Reload failed': '새로고침 실패',
        'error': '오류',
        'saving': '저장 중',
        'Save failed': '저장 실패',
        'validation error': '검증 오류',
        'Saved': '저장됨',
        'saved': '저장됨',
        'user is not active': '사용자가 활성 상태가 아닙니다',
        'authentication failed': '인증에 실패했습니다',
        'user page.': '사용자 페이지.',
        'Forbidden': '접근 금지',
        'At least one activity is required.': '최소 한 개의 액티비티가 필요합니다.',
        'Untitled': '제목 없음',
        'Every activity must have a title.': '모든 액티비티에는 제목이 있어야 합니다.',
        'Activity titles must be 100 characters or fewer.': '액티비티 제목은 100자 이하여야 합니다.',
        'Activity kind must be one of: %(choices)s.': '액티비티 종류는 다음 중 하나여야 합니다: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': '액티비티 노드 유형은 다음 중 하나여야 합니다: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': '액티비티 "%(title)s": gateway 노드는 kind=dummy를 사용해야 합니다.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': '액티비티 "%(title)s": %(node_type)s 노드는 autostart 활성화를 권장합니다.',
        'Activity "%(title)s": script nodes should enable autofinish.': '액티비티 "%(title)s": script 노드는 autofinish 활성화를 권장합니다.',
        'Activity "%(title)s": notification nodes should not use form_class.': '액티비티 "%(title)s": notification 노드는 form_class를 사용하지 않아야 합니다.',
        'Activity titles must be unique.': '액티비티 제목은 고유해야 합니다.',
        'Begin activity must exist in the workflow.': '시작 액티비티가 워크플로에 존재해야 합니다.',
        'End activity must exist in the workflow.': '종료 액티비티가 워크플로에 존재해야 합니다.',
        'Begin activity is required.': '시작 액티비티는 필수입니다.',
        'End activity is required.': '종료 액티비티는 필수입니다.',
        'Begin and End activities must be different.': '시작 액티비티와 종료 액티비티는 서로 달라야 합니다.',
        'At least one transition is required.': '최소 한 개의 전이가 필요합니다.',
        'Transitions must connect valid activities.': '전이는 유효한 액티비티를 연결해야 합니다.',
        'Transitions cannot point to the same activity.': '전이가 같은 액티비티를 가리킬 수 없습니다.',
        'Transitions must have a name or condition.': '전이에는 이름 또는 조건이 필요합니다.',
        'Duplicate transitions are not allowed.': '중복 전이는 허용되지 않습니다.',
        'All activities must be connected by at least one transition.': '모든 액티비티는 최소 한 개의 전이로 연결되어야 합니다.',
        'Begin activity cannot have incoming transitions.': '시작 액티비티에는 들어오는 전이가 있으면 안 됩니다.',
        'Begin activity must have at least one outgoing transition.': '시작 액티비티에는 최소 한 개의 나가는 전이가 필요합니다.',
        'End activity cannot have outgoing transitions.': '종료 액티비티에는 나가는 전이가 있으면 안 됩니다.',
        'End activity must have at least one incoming transition.': '종료 액티비티에는 최소 한 개의 들어오는 전이가 필요합니다.',
        'Only one default (empty) transition is allowed per activity.': '각 액티비티당 기본(빈) 전이는 하나만 허용됩니다.',
        'All activities must be reachable from Begin.': '모든 액티비티는 Begin에서 도달 가능해야 합니다.',
    },
    Path('goflow/locale/fr/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Moniteur de workflow',
        'Instances': 'Instances',
        'Total': 'Total',
        'Running': 'En cours',
        'Active': 'Actif',
        'Complete': 'Terminé',
        'Workitems': 'Éléments de travail',
        'Inactive': 'Inactif',
        'Blocked': 'Bloqué',
        'Fallout': 'Anomalie',
        'Warned': 'Averti',
        'Breached': 'Dépassé',
        'Top Processes': 'Principaux processus',
        'Process': 'Processus',
        'No data': 'Aucune donnée',
        'Recent Audit Events': 'Événements d’audit récents',
        'Time': 'Heure',
        'Action': 'Action',
        'Actor': 'Acteur',
        'No events': 'Aucun événement',
        'Recent Fallout': 'Anomalies récentes',
        'Workitem': 'Élément de travail',
        'Activity': 'Activité',
        'Updated': 'Mis à jour',
        'No fallout': 'Aucune anomalie',
        'Sample Task': 'Tâche exemple',
        'Request #123': 'Demande #123',
        'Urgent': 'Urgent',
        'Needs review': 'Nécessite une revue',
        'Comment': 'Commentaire',
        'Approve': 'Approuver',
        'Reject': 'Rejeter',
        'process %s disabled.': 'processus %s désactivé.',
        'completion page.': 'page de finalisation.',
        'Welcome,': 'Bienvenue,',
        'Change password': 'Changer le mot de passe',
        'Log out': 'Se déconnecter',
        'Log in': 'Se connecter',
        'Workflow Designer': 'Concepteur de workflow',
        'Status': 'Statut',
        'idle': 'inactif',
        'Process Settings': 'Paramètres du processus',
        'Begin Activity': 'Activité de début',
        'End Activity': 'Activité de fin',
        'Save': 'Enregistrer',
        'Reload': 'Recharger',
        'Undo': 'Annuler',
        'Redo': 'Rétablir',
        'Delete Selected': 'Supprimer la sélection',
        'Shortcuts': 'Raccourcis',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S Enregistrer',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R Recharger',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z Annuler',
        'Del Delete': 'Suppr Effacer',
        'Activities': 'Activités',
        'Title': 'Titre',
        'Start': 'Début',
        'Kind': 'Type',
        'Node Type': 'Type de nœud',
        'Form Template': 'Modèle de formulaire',
        'Form Class': 'Classe de formulaire',
        'Autostart': 'Démarrage auto',
        'Autofinish': 'Fin auto',
        'Add Activity': 'Ajouter une activité',
        'Transitions': 'Transitions',
        'From': 'De',
        'To': 'Vers',
        'Name': 'Nom',
        'approve': 'approuver',
        'Condition': 'Condition',
        'Add Transition': 'Ajouter une transition',
        'Canvas': 'Canvas',
        'Keyboard Shortcuts': 'Raccourcis clavier',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S : Enregistrer',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R : Recharger',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z : Annuler',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y : Rétablir',
        'Delete/Backspace: Delete selected': 'Suppr/Retour arrière : supprimer la sélection',
        'Double-click node: Rename': 'Double-clic sur le nœud : renommer',
        'Click edge: Edit label/condition': 'Cliquer sur l’arête : modifier libellé/condition',
        'Close': 'Fermer',
        'Validation errors': 'Erreurs de validation',
        'Rename activity': 'Renommer l’activité',
        'Transition condition or name': 'Condition ou nom de transition',
        'loading': 'chargement',
        'Reloaded': 'Rechargé',
        'ready': 'prêt',
        'Reload failed': 'Échec du rechargement',
        'error': 'erreur',
        'saving': 'enregistrement',
        'Save failed': 'Échec de l’enregistrement',
        'validation error': 'erreur de validation',
        'Saved': 'Enregistré',
        'saved': 'enregistré',
        'user is not active': 'l’utilisateur n’est pas actif',
        'authentication failed': 'échec de l’authentification',
        'user page.': 'page utilisateur.',
        'Forbidden': 'Interdit',
        'At least one activity is required.': 'Au moins une activité est requise.',
        'Untitled': 'Sans titre',
        'Every activity must have a title.': 'Chaque activité doit avoir un titre.',
        'Activity titles must be 100 characters or fewer.': 'Les titres d’activité doivent comporter 100 caractères maximum.',
        'Activity kind must be one of: %(choices)s.': 'Le type d’activité doit être l’un de : %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'Le type de nœud d’activité doit être l’un de : %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Activité "%(title)s" : les nœuds gateway doivent utiliser kind=dummy.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Activité "%(title)s" : les nœuds %(node_type)s devraient activer autostart.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Activité "%(title)s" : les nœuds script devraient activer autofinish.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Activité "%(title)s" : les nœuds notification ne doivent pas utiliser form_class.',
        'Activity titles must be unique.': 'Les titres d’activité doivent être uniques.',
        'Begin activity must exist in the workflow.': 'L’activité de début doit exister dans le workflow.',
        'End activity must exist in the workflow.': 'L’activité de fin doit exister dans le workflow.',
        'Begin activity is required.': 'L’activité de début est requise.',
        'End activity is required.': 'L’activité de fin est requise.',
        'Begin and End activities must be different.': 'Les activités de début et de fin doivent être différentes.',
        'At least one transition is required.': 'Au moins une transition est requise.',
        'Transitions must connect valid activities.': 'Les transitions doivent relier des activités valides.',
        'Transitions cannot point to the same activity.': 'Les transitions ne peuvent pas pointer vers la même activité.',
        'Transitions must have a name or condition.': 'Les transitions doivent avoir un nom ou une condition.',
        'Duplicate transitions are not allowed.': 'Les transitions dupliquées ne sont pas autorisées.',
        'All activities must be connected by at least one transition.': 'Toutes les activités doivent être reliées par au moins une transition.',
        'Begin activity cannot have incoming transitions.': 'L’activité de début ne peut pas avoir de transitions entrantes.',
        'Begin activity must have at least one outgoing transition.': 'L’activité de début doit avoir au moins une transition sortante.',
        'End activity cannot have outgoing transitions.': 'L’activité de fin ne peut pas avoir de transitions sortantes.',
        'End activity must have at least one incoming transition.': 'L’activité de fin doit avoir au moins une transition entrante.',
        'Only one default (empty) transition is allowed per activity.': 'Une seule transition par défaut (vide) est autorisée par activité.',
        'All activities must be reachable from Begin.': 'Toutes les activités doivent être atteignables depuis Begin.',
    },
    Path('leavedemo/locale/ko/LC_MESSAGES/django.po'): {
        'English': '영어',
        'French': '프랑스어',
        'Simplified Chinese': '중국어 간체',
        'Traditional Chinese': '중국어 번체',
        'Japanese': '일본어',
        'Korean': '한국어',
        'German': '독일어',
        'Spanish': '스페인어',
        'Italian': '이탈리아어',
        'Portuguese': '포르투갈어',
        'Russian': '러시아어',
        'Log in': '로그인',
    },
    Path('leavedemo/locale/fr/LC_MESSAGES/django.po'): {
        'English': 'Anglais',
        'French': 'Français',
        'Simplified Chinese': 'Chinois simplifié',
        'Traditional Chinese': 'Chinois traditionnel',
        'Japanese': 'Japonais',
        'Korean': 'Coréen',
        'German': 'Allemand',
        'Spanish': 'Espagnol',
        'Italian': 'Italien',
        'Portuguese': 'Portugais',
        'Russian': 'Russe',
        'Log in': 'Se connecter',
    },
    Path('sampleproject/locale/ko/LC_MESSAGES/django.po'): {
        'English': '영어',
        'French': '프랑스어',
        'Simplified Chinese': '중국어 간체',
        'Traditional Chinese': '중국어 번체',
        'Japanese': '일본어',
        'Korean': '한국어',
        'German': '독일어',
        'Spanish': '스페인어',
        'Italian': '이탈리아어',
        'Portuguese': '포르투갈어',
        'Russian': '러시아어',
    },
    Path('sampleproject/locale/fr/LC_MESSAGES/django.po'): {
        'English': 'Anglais',
        'French': 'Français',
        'Simplified Chinese': 'Chinois simplifié',
        'Traditional Chinese': 'Chinois traditionnel',
        'Japanese': 'Japonais',
        'Korean': 'Coréen',
        'German': 'Allemand',
        'Spanish': 'Espagnol',
        'Italian': 'Italien',
        'Portuguese': 'Portugais',
        'Russian': 'Russe',
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