from pathlib import Path


TARGETS = {
    Path('goflow/locale/es/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Monitor de flujo de trabajo',
        'Instances': 'Instancias',
        'Total': 'Total',
        'Running': 'En ejecución',
        'Active': 'Activo',
        'Complete': 'Completado',
        'Workitems': 'Elementos de trabajo',
        'Inactive': 'Inactivo',
        'Blocked': 'Bloqueado',
        'Fallout': 'Incidencia',
        'Warned': 'Advertido',
        'Breached': 'Incumplido',
        'Top Processes': 'Procesos principales',
        'Process': 'Proceso',
        'No data': 'Sin datos',
        'Recent Audit Events': 'Eventos de auditoría recientes',
        'Time': 'Hora',
        'Action': 'Acción',
        'Actor': 'Actor',
        'No events': 'Sin eventos',
        'Recent Fallout': 'Incidencias recientes',
        'Workitem': 'Elemento de trabajo',
        'Activity': 'Actividad',
        'Updated': 'Actualizado',
        'No fallout': 'Sin incidencias',
        'Sample Task': 'Tarea de ejemplo',
        'Request #123': 'Solicitud #123',
        'Urgent': 'Urgente',
        'Needs review': 'Requiere revisión',
        'Comment': 'Comentario',
        'Approve': 'Aprobar',
        'Reject': 'Rechazar',
        'process %s disabled.': 'proceso %s deshabilitado.',
        'completion page.': 'página de finalización.',
        'Welcome,': 'Bienvenido,',
        'Change password': 'Cambiar contraseña',
        'Log out': 'Cerrar sesión',
        'Log in': 'Iniciar sesión',
        'Workflow Designer': 'Diseñador de flujo de trabajo',
        'Status': 'Estado',
        'idle': 'inactivo',
        'Process Settings': 'Configuración del proceso',
        'Begin Activity': 'Actividad inicial',
        'End Activity': 'Actividad final',
        'Save': 'Guardar',
        'Reload': 'Recargar',
        'Undo': 'Deshacer',
        'Redo': 'Rehacer',
        'Delete Selected': 'Eliminar selección',
        'Shortcuts': 'Atajos',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S Guardar',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R Recargar',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z Deshacer',
        'Del Delete': 'Supr Eliminar',
        'Activities': 'Actividades',
        'Title': 'Título',
        'Start': 'Inicio',
        'Kind': 'Tipo',
        'Node Type': 'Tipo de nodo',
        'Form Template': 'Plantilla de formulario',
        'Form Class': 'Clase de formulario',
        'Autostart': 'Inicio automático',
        'Autofinish': 'Finalización automática',
        'Add Activity': 'Agregar actividad',
        'Transitions': 'Transiciones',
        'From': 'Desde',
        'To': 'Hacia',
        'Name': 'Nombre',
        'approve': 'aprobar',
        'Condition': 'Condición',
        'Add Transition': 'Agregar transición',
        'Canvas': 'Lienzo',
        'Keyboard Shortcuts': 'Atajos de teclado',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: Guardar',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: Recargar',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: Deshacer',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: Rehacer',
        'Delete/Backspace: Delete selected': 'Supr/Retroceso: eliminar selección',
        'Double-click node: Rename': 'Doble clic en nodo: renombrar',
        'Click edge: Edit label/condition': 'Clic en arista: editar etiqueta/condición',
        'Close': 'Cerrar',
        'Validation errors': 'Errores de validación',
        'Rename activity': 'Renombrar actividad',
        'Transition condition or name': 'Condición o nombre de transición',
        'loading': 'cargando',
        'Reloaded': 'Recargado',
        'ready': 'listo',
        'Reload failed': 'Error al recargar',
        'error': 'error',
        'saving': 'guardando',
        'Save failed': 'Error al guardar',
        'validation error': 'error de validación',
        'Saved': 'Guardado',
        'saved': 'guardado',
        'user is not active': 'el usuario no está activo',
        'authentication failed': 'autenticación fallida',
        'user page.': 'página de usuario.',
        'Forbidden': 'Prohibido',
        'At least one activity is required.': 'Se requiere al menos una actividad.',
        'Untitled': 'Sin título',
        'Every activity must have a title.': 'Cada actividad debe tener un título.',
        'Activity titles must be 100 characters or fewer.': 'Los títulos de actividad deben tener 100 caracteres o menos.',
        'Activity kind must be one of: %(choices)s.': 'El tipo de actividad debe ser uno de: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'El tipo de nodo de actividad debe ser uno de: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Actividad "%(title)s": los nodos gateway deben usar kind=dummy.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Actividad "%(title)s": los nodos %(node_type)s deberían habilitar autostart.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Actividad "%(title)s": los nodos script deberían habilitar autofinish.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Actividad "%(title)s": los nodos notification no deben usar form_class.',
        'Activity titles must be unique.': 'Los títulos de actividad deben ser únicos.',
        'Begin activity must exist in the workflow.': 'La actividad inicial debe existir en el flujo.',
        'End activity must exist in the workflow.': 'La actividad final debe existir en el flujo.',
        'Begin activity is required.': 'La actividad inicial es obligatoria.',
        'End activity is required.': 'La actividad final es obligatoria.',
        'Begin and End activities must be different.': 'Las actividades inicial y final deben ser distintas.',
        'At least one transition is required.': 'Se requiere al menos una transición.',
        'Transitions must connect valid activities.': 'Las transiciones deben conectar actividades válidas.',
        'Transitions cannot point to the same activity.': 'Las transiciones no pueden apuntar a la misma actividad.',
        'Transitions must have a name or condition.': 'Las transiciones deben tener un nombre o una condición.',
        'Duplicate transitions are not allowed.': 'No se permiten transiciones duplicadas.',
        'All activities must be connected by at least one transition.': 'Todas las actividades deben estar conectadas por al menos una transición.',
        'Begin activity cannot have incoming transitions.': 'La actividad inicial no puede tener transiciones entrantes.',
        'Begin activity must have at least one outgoing transition.': 'La actividad inicial debe tener al menos una transición saliente.',
        'End activity cannot have outgoing transitions.': 'La actividad final no puede tener transiciones salientes.',
        'End activity must have at least one incoming transition.': 'La actividad final debe tener al menos una transición entrante.',
        'Only one default (empty) transition is allowed per activity.': 'Solo se permite una transición predeterminada (vacía) por actividad.',
        'All activities must be reachable from Begin.': 'Todas las actividades deben ser alcanzables desde Begin.',
    },
    Path('goflow/locale/pt/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Monitor de workflow',
        'Instances': 'Instâncias',
        'Total': 'Total',
        'Running': 'Em execução',
        'Active': 'Ativo',
        'Complete': 'Concluído',
        'Workitems': 'Itens de trabalho',
        'Inactive': 'Inativo',
        'Blocked': 'Bloqueado',
        'Fallout': 'Falha',
        'Warned': 'Avisado',
        'Breached': 'Violado',
        'Top Processes': 'Principais processos',
        'Process': 'Processo',
        'No data': 'Sem dados',
        'Recent Audit Events': 'Eventos de auditoria recentes',
        'Time': 'Hora',
        'Action': 'Ação',
        'Actor': 'Ator',
        'No events': 'Sem eventos',
        'Recent Fallout': 'Falhas recentes',
        'Workitem': 'Item de trabalho',
        'Activity': 'Atividade',
        'Updated': 'Atualizado',
        'No fallout': 'Sem falhas',
        'Sample Task': 'Tarefa de exemplo',
        'Request #123': 'Solicitação #123',
        'Urgent': 'Urgente',
        'Needs review': 'Precisa de revisão',
        'Comment': 'Comentário',
        'Approve': 'Aprovar',
        'Reject': 'Rejeitar',
        'process %s disabled.': 'processo %s desativado.',
        'completion page.': 'página de conclusão.',
        'Welcome,': 'Bem-vindo,',
        'Change password': 'Alterar senha',
        'Log out': 'Sair',
        'Log in': 'Entrar',
        'Workflow Designer': 'Designer de workflow',
        'Status': 'Status',
        'idle': 'inativo',
        'Process Settings': 'Configurações do processo',
        'Begin Activity': 'Atividade inicial',
        'End Activity': 'Atividade final',
        'Save': 'Salvar',
        'Reload': 'Recarregar',
        'Undo': 'Desfazer',
        'Redo': 'Refazer',
        'Delete Selected': 'Excluir selecionados',
        'Shortcuts': 'Atalhos',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S Salvar',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R Recarregar',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z Desfazer',
        'Del Delete': 'Del Excluir',
        'Activities': 'Atividades',
        'Title': 'Título',
        'Start': 'Início',
        'Kind': 'Tipo',
        'Node Type': 'Tipo de nó',
        'Form Template': 'Template de formulário',
        'Form Class': 'Classe de formulário',
        'Autostart': 'Início automático',
        'Autofinish': 'Finalização automática',
        'Add Activity': 'Adicionar atividade',
        'Transitions': 'Transições',
        'From': 'De',
        'To': 'Para',
        'Name': 'Nome',
        'approve': 'aprovar',
        'Condition': 'Condição',
        'Add Transition': 'Adicionar transição',
        'Canvas': 'Canvas',
        'Keyboard Shortcuts': 'Atalhos de teclado',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: Salvar',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: Recarregar',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: Desfazer',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: Refazer',
        'Delete/Backspace: Delete selected': 'Del/Backspace: excluir selecionados',
        'Double-click node: Rename': 'Duplo clique no nó: renomear',
        'Click edge: Edit label/condition': 'Clique na aresta: editar rótulo/condição',
        'Close': 'Fechar',
        'Validation errors': 'Erros de validação',
        'Rename activity': 'Renomear atividade',
        'Transition condition or name': 'Condição ou nome da transição',
        'loading': 'carregando',
        'Reloaded': 'Recarregado',
        'ready': 'pronto',
        'Reload failed': 'Falha ao recarregar',
        'error': 'erro',
        'saving': 'salvando',
        'Save failed': 'Falha ao salvar',
        'validation error': 'erro de validação',
        'Saved': 'Salvo',
        'saved': 'salvo',
        'user is not active': 'o usuário não está ativo',
        'authentication failed': 'falha na autenticação',
        'user page.': 'página do usuário.',
        'Forbidden': 'Proibido',
        'At least one activity is required.': 'Pelo menos uma atividade é obrigatória.',
        'Untitled': 'Sem título',
        'Every activity must have a title.': 'Toda atividade deve ter um título.',
        'Activity titles must be 100 characters or fewer.': 'Os títulos das atividades devem ter no máximo 100 caracteres.',
        'Activity kind must be one of: %(choices)s.': 'O tipo de atividade deve ser um dos seguintes: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'O tipo de nó da atividade deve ser um dos seguintes: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Atividade "%(title)s": nós gateway devem usar kind=dummy.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Atividade "%(title)s": nós %(node_type)s devem habilitar autostart.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Atividade "%(title)s": nós script devem habilitar autofinish.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Atividade "%(title)s": nós notification não devem usar form_class.',
        'Activity titles must be unique.': 'Os títulos das atividades devem ser únicos.',
        'Begin activity must exist in the workflow.': 'A atividade inicial deve existir no workflow.',
        'End activity must exist in the workflow.': 'A atividade final deve existir no workflow.',
        'Begin activity is required.': 'A atividade inicial é obrigatória.',
        'End activity is required.': 'A atividade final é obrigatória.',
        'Begin and End activities must be different.': 'As atividades inicial e final devem ser diferentes.',
        'At least one transition is required.': 'Pelo menos uma transição é obrigatória.',
        'Transitions must connect valid activities.': 'As transições devem conectar atividades válidas.',
        'Transitions cannot point to the same activity.': 'As transições não podem apontar para a mesma atividade.',
        'Transitions must have a name or condition.': 'As transições devem ter um nome ou condição.',
        'Duplicate transitions are not allowed.': 'Transições duplicadas não são permitidas.',
        'All activities must be connected by at least one transition.': 'Todas as atividades devem estar conectadas por pelo menos uma transição.',
        'Begin activity cannot have incoming transitions.': 'A atividade inicial não pode ter transições de entrada.',
        'Begin activity must have at least one outgoing transition.': 'A atividade inicial deve ter pelo menos uma transição de saída.',
        'End activity cannot have outgoing transitions.': 'A atividade final não pode ter transições de saída.',
        'End activity must have at least one incoming transition.': 'A atividade final deve ter pelo menos uma transição de entrada.',
        'Only one default (empty) transition is allowed per activity.': 'Somente uma transição padrão (vazia) é permitida por atividade.',
        'All activities must be reachable from Begin.': 'Todas as atividades devem ser alcançáveis a partir de Begin.',
    },
    Path('leavedemo/locale/es/LC_MESSAGES/django.po'): {
        'English': 'Inglés',
        'French': 'Francés',
        'Simplified Chinese': 'Chino simplificado',
        'Traditional Chinese': 'Chino tradicional',
        'Japanese': 'Japonés',
        'Korean': 'Coreano',
        'German': 'Alemán',
        'Spanish': 'Español',
        'Italian': 'Italiano',
        'Portuguese': 'Portugués',
        'Russian': 'Ruso',
        'Log in': 'Iniciar sesión',
    },
    Path('leavedemo/locale/pt/LC_MESSAGES/django.po'): {
        'English': 'Inglês',
        'French': 'Francês',
        'Simplified Chinese': 'Chinês simplificado',
        'Traditional Chinese': 'Chinês tradicional',
        'Japanese': 'Japonês',
        'Korean': 'Coreano',
        'German': 'Alemão',
        'Spanish': 'Espanhol',
        'Italian': 'Italiano',
        'Portuguese': 'Português',
        'Russian': 'Russo',
        'Log in': 'Entrar',
    },
    Path('sampleproject/locale/es/LC_MESSAGES/django.po'): {
        'English': 'Inglés',
        'French': 'Francés',
        'Simplified Chinese': 'Chino simplificado',
        'Traditional Chinese': 'Chino tradicional',
        'Japanese': 'Japonés',
        'Korean': 'Coreano',
        'German': 'Alemán',
        'Spanish': 'Español',
        'Italian': 'Italiano',
        'Portuguese': 'Portugués',
        'Russian': 'Ruso',
    },
    Path('sampleproject/locale/pt/LC_MESSAGES/django.po'): {
        'English': 'Inglês',
        'French': 'Francês',
        'Simplified Chinese': 'Chinês simplificado',
        'Traditional Chinese': 'Chinês tradicional',
        'Japanese': 'Japonês',
        'Korean': 'Coreano',
        'German': 'Alemão',
        'Spanish': 'Espanhol',
        'Italian': 'Italiano',
        'Portuguese': 'Português',
        'Russian': 'Russo',
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