from pathlib import Path


TARGETS = {
    Path('goflow/locale/de/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Workflow-Monitor',
        'Instances': 'Instanzen',
        'Total': 'Gesamt',
        'Running': 'Laufend',
        'Active': 'Aktiv',
        'Complete': 'Abgeschlossen',
        'Workitems': 'Arbeitselemente',
        'Inactive': 'Inaktiv',
        'Blocked': 'Blockiert',
        'Fallout': 'Fehlerfall',
        'Warned': 'Gewarnt',
        'Breached': 'Verletzt',
        'Top Processes': 'Top-Prozesse',
        'Process': 'Prozess',
        'No data': 'Keine Daten',
        'Recent Audit Events': 'Letzte Audit-Ereignisse',
        'Time': 'Zeit',
        'Action': 'Aktion',
        'Actor': 'Akteur',
        'No events': 'Keine Ereignisse',
        'Recent Fallout': 'Letzte Fehlerfälle',
        'Workitem': 'Arbeitselement',
        'Activity': 'Aktivität',
        'Updated': 'Aktualisiert',
        'No fallout': 'Keine Fehlerfälle',
        'Sample Task': 'Beispielaufgabe',
        'Request #123': 'Anfrage #123',
        'Urgent': 'Dringend',
        'Needs review': 'Überprüfung erforderlich',
        'Comment': 'Kommentar',
        'Approve': 'Genehmigen',
        'Reject': 'Ablehnen',
        'process %s disabled.': 'Prozess %s deaktiviert.',
        'completion page.': 'Abschlussseite.',
        'Welcome,': 'Willkommen,',
        'Change password': 'Passwort ändern',
        'Log out': 'Abmelden',
        'Log in': 'Anmelden',
        'Workflow Designer': 'Workflow-Designer',
        'Status': 'Status',
        'idle': 'inaktiv',
        'Process Settings': 'Prozesseinstellungen',
        'Begin Activity': 'Startaktivität',
        'End Activity': 'Endaktivität',
        'Save': 'Speichern',
        'Reload': 'Neu laden',
        'Undo': 'Rückgängig',
        'Redo': 'Wiederholen',
        'Delete Selected': 'Auswahl löschen',
        'Shortcuts': 'Kurzbefehle',
        'Ctrl/Cmd+S Save': 'Strg/Cmd+S Speichern',
        'Ctrl/Cmd+R Reload': 'Strg/Cmd+R Neu laden',
        'Ctrl/Cmd+Z Undo': 'Strg/Cmd+Z Rückgängig',
        'Del Delete': 'Entf Löschen',
        'Activities': 'Aktivitäten',
        'Title': 'Titel',
        'Start': 'Start',
        'Kind': 'Typ',
        'Node Type': 'Knotentyp',
        'Form Template': 'Formularvorlage',
        'Form Class': 'Formularklasse',
        'Autostart': 'Autostart',
        'Autofinish': 'Autoabschluss',
        'Add Activity': 'Aktivität hinzufügen',
        'Transitions': 'Übergänge',
        'From': 'Von',
        'To': 'Nach',
        'Name': 'Name',
        'approve': 'genehmigen',
        'Condition': 'Bedingung',
        'Add Transition': 'Übergang hinzufügen',
        'Canvas': 'Zeichenfläche',
        'Keyboard Shortcuts': 'Tastaturkürzel',
        'Ctrl/Cmd + S: Save': 'Strg/Cmd + S: Speichern',
        'Ctrl/Cmd + R: Reload': 'Strg/Cmd + R: Neu laden',
        'Ctrl/Cmd + Z: Undo': 'Strg/Cmd + Z: Rückgängig',
        'Ctrl/Cmd + Y: Redo': 'Strg/Cmd + Y: Wiederholen',
        'Delete/Backspace: Delete selected': 'Entf/Backspace: Auswahl löschen',
        'Double-click node: Rename': 'Doppelklick auf Knoten: Umbenennen',
        'Click edge: Edit label/condition': 'Kante anklicken: Label/Bedingung bearbeiten',
        'Close': 'Schließen',
        'Validation errors': 'Validierungsfehler',
        'Rename activity': 'Aktivität umbenennen',
        'Transition condition or name': 'Übergangsbedingung oder Name',
        'loading': 'lädt',
        'Reloaded': 'Neu geladen',
        'ready': 'bereit',
        'Reload failed': 'Neuladen fehlgeschlagen',
        'error': 'Fehler',
        'saving': 'speichert',
        'Save failed': 'Speichern fehlgeschlagen',
        'validation error': 'Validierungsfehler',
        'Saved': 'Gespeichert',
        'saved': 'gespeichert',
        'user is not active': 'Benutzer ist nicht aktiv',
        'authentication failed': 'Authentifizierung fehlgeschlagen',
        'user page.': 'Benutzerseite.',
        'Forbidden': 'Verboten',
        'At least one activity is required.': 'Mindestens eine Aktivität ist erforderlich.',
        'Untitled': 'Ohne Titel',
        'Every activity must have a title.': 'Jede Aktivität muss einen Titel haben.',
        'Activity titles must be 100 characters or fewer.': 'Aktivitätstitel dürfen höchstens 100 Zeichen lang sein.',
        'Activity kind must be one of: %(choices)s.': 'Aktivitätstyp muss einer der folgenden sein: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'Aktivitätsknotentyp muss einer der folgenden sein: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Aktivität "%(title)s": Gateway-Knoten müssen kind=dummy verwenden.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Aktivität "%(title)s": Bei %(node_type)s-Knoten sollte autostart aktiviert sein.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Aktivität "%(title)s": Bei script-Knoten sollte autofinish aktiviert sein.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Aktivität "%(title)s": notification-Knoten sollten form_class nicht verwenden.',
        'Activity titles must be unique.': 'Aktivitätstitel müssen eindeutig sein.',
        'Begin activity must exist in the workflow.': 'Die Startaktivität muss im Workflow vorhanden sein.',
        'End activity must exist in the workflow.': 'Die Endaktivität muss im Workflow vorhanden sein.',
        'Begin activity is required.': 'Eine Startaktivität ist erforderlich.',
        'End activity is required.': 'Eine Endaktivität ist erforderlich.',
        'Begin and End activities must be different.': 'Start- und Endaktivität müssen unterschiedlich sein.',
        'At least one transition is required.': 'Mindestens ein Übergang ist erforderlich.',
        'Transitions must connect valid activities.': 'Übergänge müssen gültige Aktivitäten verbinden.',
        'Transitions cannot point to the same activity.': 'Übergänge dürfen nicht auf dieselbe Aktivität zeigen.',
        'Transitions must have a name or condition.': 'Übergänge müssen einen Namen oder eine Bedingung haben.',
        'Duplicate transitions are not allowed.': 'Doppelte Übergänge sind nicht erlaubt.',
        'All activities must be connected by at least one transition.': 'Alle Aktivitäten müssen durch mindestens einen Übergang verbunden sein.',
        'Begin activity cannot have incoming transitions.': 'Die Startaktivität darf keine eingehenden Übergänge haben.',
        'Begin activity must have at least one outgoing transition.': 'Die Startaktivität muss mindestens einen ausgehenden Übergang haben.',
        'End activity cannot have outgoing transitions.': 'Die Endaktivität darf keine ausgehenden Übergänge haben.',
        'End activity must have at least one incoming transition.': 'Die Endaktivität muss mindestens einen eingehenden Übergang haben.',
        'Only one default (empty) transition is allowed per activity.': 'Pro Aktivität ist nur ein Standardübergang (leer) erlaubt.',
        'All activities must be reachable from Begin.': 'Alle Aktivitäten müssen von Begin aus erreichbar sein.',
    },
    Path('goflow/locale/it/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'Monitor del workflow',
        'Instances': 'Istanze',
        'Total': 'Totale',
        'Running': 'In esecuzione',
        'Active': 'Attivo',
        'Complete': 'Completato',
        'Workitems': 'Elementi di lavoro',
        'Inactive': 'Inattivo',
        'Blocked': 'Bloccato',
        'Fallout': 'Errore',
        'Warned': 'Avvisato',
        'Breached': 'Superato',
        'Top Processes': 'Processi principali',
        'Process': 'Processo',
        'No data': 'Nessun dato',
        'Recent Audit Events': 'Eventi di audit recenti',
        'Time': 'Ora',
        'Action': 'Azione',
        'Actor': 'Attore',
        'No events': 'Nessun evento',
        'Recent Fallout': 'Errori recenti',
        'Workitem': 'Elemento di lavoro',
        'Activity': 'Attività',
        'Updated': 'Aggiornato',
        'No fallout': 'Nessun errore',
        'Sample Task': 'Attività di esempio',
        'Request #123': 'Richiesta #123',
        'Urgent': 'Urgente',
        'Needs review': 'Richiede revisione',
        'Comment': 'Commento',
        'Approve': 'Approva',
        'Reject': 'Rifiuta',
        'process %s disabled.': 'processo %s disabilitato.',
        'completion page.': 'pagina di completamento.',
        'Welcome,': 'Benvenuto,',
        'Change password': 'Cambia password',
        'Log out': 'Disconnetti',
        'Log in': 'Accedi',
        'Workflow Designer': 'Designer del workflow',
        'Status': 'Stato',
        'idle': 'inattivo',
        'Process Settings': 'Impostazioni processo',
        'Begin Activity': 'Attività iniziale',
        'End Activity': 'Attività finale',
        'Save': 'Salva',
        'Reload': 'Ricarica',
        'Undo': 'Annulla',
        'Redo': 'Ripeti',
        'Delete Selected': 'Elimina selezionati',
        'Shortcuts': 'Scorciatoie',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S Salva',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R Ricarica',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z Annulla',
        'Del Delete': 'Canc Elimina',
        'Activities': 'Attività',
        'Title': 'Titolo',
        'Start': 'Inizio',
        'Kind': 'Tipo',
        'Node Type': 'Tipo nodo',
        'Form Template': 'Template modulo',
        'Form Class': 'Classe modulo',
        'Autostart': 'Avvio automatico',
        'Autofinish': 'Chiusura automatica',
        'Add Activity': 'Aggiungi attività',
        'Transitions': 'Transizioni',
        'From': 'Da',
        'To': 'A',
        'Name': 'Nome',
        'approve': 'approva',
        'Condition': 'Condizione',
        'Add Transition': 'Aggiungi transizione',
        'Canvas': 'Canvas',
        'Keyboard Shortcuts': 'Scorciatoie da tastiera',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: Salva',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: Ricarica',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: Annulla',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: Ripeti',
        'Delete/Backspace: Delete selected': 'Canc/Backspace: elimina selezionati',
        'Double-click node: Rename': 'Doppio clic sul nodo: rinomina',
        'Click edge: Edit label/condition': 'Clic sul bordo: modifica etichetta/condizione',
        'Close': 'Chiudi',
        'Validation errors': 'Errori di validazione',
        'Rename activity': 'Rinomina attività',
        'Transition condition or name': 'Condizione o nome transizione',
        'loading': 'caricamento',
        'Reloaded': 'Ricaricato',
        'ready': 'pronto',
        'Reload failed': 'Ricarica non riuscita',
        'error': 'errore',
        'saving': 'salvataggio',
        'Save failed': 'Salvataggio non riuscito',
        'validation error': 'errore di validazione',
        'Saved': 'Salvato',
        'saved': 'salvato',
        'user is not active': 'utente non attivo',
        'authentication failed': 'autenticazione fallita',
        'user page.': 'pagina utente.',
        'Forbidden': 'Accesso negato',
        'At least one activity is required.': 'È richiesta almeno un’attività.',
        'Untitled': 'Senza titolo',
        'Every activity must have a title.': 'Ogni attività deve avere un titolo.',
        'Activity titles must be 100 characters or fewer.': 'I titoli delle attività devono avere al massimo 100 caratteri.',
        'Activity kind must be one of: %(choices)s.': 'Il tipo di attività deve essere uno tra: %(choices)s.',
        'Activity node type must be one of: %(choices)s.': 'Il tipo di nodo attività deve essere uno tra: %(choices)s.',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'Attività "%(title)s": i nodi gateway devono usare kind=dummy.',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'Attività "%(title)s": i nodi %(node_type)s dovrebbero abilitare autostart.',
        'Activity "%(title)s": script nodes should enable autofinish.': 'Attività "%(title)s": i nodi script dovrebbero abilitare autofinish.',
        'Activity "%(title)s": notification nodes should not use form_class.': 'Attività "%(title)s": i nodi notification non dovrebbero usare form_class.',
        'Activity titles must be unique.': 'I titoli delle attività devono essere univoci.',
        'Begin activity must exist in the workflow.': 'L’attività iniziale deve esistere nel workflow.',
        'End activity must exist in the workflow.': 'L’attività finale deve esistere nel workflow.',
        'Begin activity is required.': 'L’attività iniziale è obbligatoria.',
        'End activity is required.': 'L’attività finale è obbligatoria.',
        'Begin and End activities must be different.': 'Le attività iniziale e finale devono essere diverse.',
        'At least one transition is required.': 'È richiesta almeno una transizione.',
        'Transitions must connect valid activities.': 'Le transizioni devono collegare attività valide.',
        'Transitions cannot point to the same activity.': 'Le transizioni non possono puntare alla stessa attività.',
        'Transitions must have a name or condition.': 'Le transizioni devono avere un nome o una condizione.',
        'Duplicate transitions are not allowed.': 'Le transizioni duplicate non sono consentite.',
        'All activities must be connected by at least one transition.': 'Tutte le attività devono essere collegate da almeno una transizione.',
        'Begin activity cannot have incoming transitions.': 'L’attività iniziale non può avere transizioni in ingresso.',
        'Begin activity must have at least one outgoing transition.': 'L’attività iniziale deve avere almeno una transizione in uscita.',
        'End activity cannot have outgoing transitions.': 'L’attività finale non può avere transizioni in uscita.',
        'End activity must have at least one incoming transition.': 'L’attività finale deve avere almeno una transizione in ingresso.',
        'Only one default (empty) transition is allowed per activity.': 'È consentita una sola transizione predefinita (vuota) per attività.',
        'All activities must be reachable from Begin.': 'Tutte le attività devono essere raggiungibili da Begin.',
    },
    Path('leavedemo/locale/de/LC_MESSAGES/django.po'): {
        'English': 'Englisch',
        'French': 'Französisch',
        'Simplified Chinese': 'Vereinfachtes Chinesisch',
        'Traditional Chinese': 'Traditionelles Chinesisch',
        'Japanese': 'Japanisch',
        'Korean': 'Koreanisch',
        'German': 'Deutsch',
        'Spanish': 'Spanisch',
        'Italian': 'Italienisch',
        'Portuguese': 'Portugiesisch',
        'Russian': 'Russisch',
        'Log in': 'Anmelden',
    },
    Path('leavedemo/locale/it/LC_MESSAGES/django.po'): {
        'English': 'Inglese',
        'French': 'Francese',
        'Simplified Chinese': 'Cinese semplificato',
        'Traditional Chinese': 'Cinese tradizionale',
        'Japanese': 'Giapponese',
        'Korean': 'Coreano',
        'German': 'Tedesco',
        'Spanish': 'Spagnolo',
        'Italian': 'Italiano',
        'Portuguese': 'Portoghese',
        'Russian': 'Russo',
        'Log in': 'Accedi',
    },
    Path('sampleproject/locale/de/LC_MESSAGES/django.po'): {
        'English': 'Englisch',
        'French': 'Französisch',
        'Simplified Chinese': 'Vereinfachtes Chinesisch',
        'Traditional Chinese': 'Traditionelles Chinesisch',
        'Japanese': 'Japanisch',
        'Korean': 'Koreanisch',
        'German': 'Deutsch',
        'Spanish': 'Spanisch',
        'Italian': 'Italienisch',
        'Portuguese': 'Portugiesisch',
        'Russian': 'Russisch',
    },
    Path('sampleproject/locale/it/LC_MESSAGES/django.po'): {
        'English': 'Inglese',
        'French': 'Francese',
        'Simplified Chinese': 'Cinese semplificato',
        'Traditional Chinese': 'Cinese tradizionale',
        'Japanese': 'Giapponese',
        'Korean': 'Coreano',
        'German': 'Tedesco',
        'Spanish': 'Spagnolo',
        'Italian': 'Italiano',
        'Portuguese': 'Portoghese',
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