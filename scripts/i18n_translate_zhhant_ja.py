from pathlib import Path


TARGETS = {
    Path('goflow/locale/zh_Hant/LC_MESSAGES/django.po'): {
        'Workflow Monitor': '工作流程監控',
        'Instances': '實例',
        'Total': '總數',
        'Running': '執行中',
        'Active': '啟用',
        'Complete': '完成',
        'Workitems': '工作項目',
        'Inactive': '未啟用',
        'Blocked': '已阻塞',
        'Fallout': '異常',
        'Warned': '已預警',
        'Breached': '已逾期',
        'Top Processes': '熱門流程',
        'Process': '流程',
        'No data': '無資料',
        'Recent Audit Events': '最近稽核事件',
        'Time': '時間',
        'Action': '動作',
        'Actor': '操作者',
        'No events': '無事件',
        'Recent Fallout': '最近異常',
        'Workitem': '工作項目',
        'Activity': '活動',
        'Updated': '更新時間',
        'No fallout': '無異常',
        'Sample Task': '範例任務',
        'Request #123': '申請 #123',
        'Urgent': '緊急',
        'Needs review': '需要審核',
        'Comment': '註解',
        'Approve': '核准',
        'Reject': '駁回',
        'process %s disabled.': '流程 %s 已停用。',
        'completion page.': '完成頁面。',
        'Welcome,': '歡迎，',
        'Change password': '變更密碼',
        'Log out': '登出',
        'Log in': '登入',
        'Workflow Designer': '流程設計器',
        'Status': '狀態',
        'idle': '閒置',
        'Process Settings': '流程設定',
        'Begin Activity': '開始活動',
        'End Activity': '結束活動',
        'Save': '儲存',
        'Reload': '重新載入',
        'Undo': '復原',
        'Redo': '重做',
        'Delete Selected': '刪除已選項',
        'Shortcuts': '快捷鍵',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S 儲存',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R 重新載入',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z 復原',
        'Del Delete': 'Del 刪除',
        'Activities': '活動列表',
        'Title': '標題',
        'Start': '開始',
        'Kind': '類型',
        'Node Type': '節點類型',
        'Form Template': '表單範本',
        'Form Class': '表單類別',
        'Autostart': '自動啟動',
        'Autofinish': '自動完成',
        'Add Activity': '新增活動',
        'Transitions': '轉移',
        'From': '從',
        'To': '到',
        'Name': '名稱',
        'approve': '核准',
        'Condition': '條件',
        'Add Transition': '新增轉移',
        'Canvas': '畫布',
        'Keyboard Shortcuts': '鍵盤快捷鍵',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S：儲存',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R：重新載入',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z：復原',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y：重做',
        'Delete/Backspace: Delete selected': 'Delete/Backspace：刪除已選項',
        'Double-click node: Rename': '雙擊節點：重新命名',
        'Click edge: Edit label/condition': '點擊連線：編輯標籤/條件',
        'Close': '關閉',
        'Validation errors': '驗證錯誤',
        'Rename activity': '重新命名活動',
        'Transition condition or name': '轉移條件或名稱',
        'loading': '載入中',
        'Reloaded': '已重新載入',
        'ready': '就緒',
        'Reload failed': '重新載入失敗',
        'error': '錯誤',
        'saving': '儲存中',
        'Save failed': '儲存失敗',
        'validation error': '驗證錯誤',
        'Saved': '已儲存',
        'saved': '已儲存',
        'user is not active': '使用者未啟用',
        'authentication failed': '驗證失敗',
        'user page.': '使用者頁面。',
        'Forbidden': '禁止存取',
        'At least one activity is required.': '至少需要一個活動。',
        'Untitled': '未命名',
        'Every activity must have a title.': '每個活動都必須有標題。',
        'Activity titles must be 100 characters or fewer.': '活動標題不可超過 100 個字元。',
        'Activity kind must be one of: %(choices)s.': '活動類型必須是以下其中之一：%(choices)s。',
        'Activity node type must be one of: %(choices)s.': '活動節點類型必須是以下其中之一：%(choices)s。',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': '活動「%(title)s」：gateway 節點必須使用 kind=dummy。',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': '活動「%(title)s」：%(node_type)s 節點建議啟用 autostart。',
        'Activity "%(title)s": script nodes should enable autofinish.': '活動「%(title)s」：script 節點建議啟用 autofinish。',
        'Activity "%(title)s": notification nodes should not use form_class.': '活動「%(title)s」：notification 節點不應使用 form_class。',
        'Activity titles must be unique.': '活動標題必須唯一。',
        'Begin activity must exist in the workflow.': '開始活動必須存在於流程中。',
        'End activity must exist in the workflow.': '結束活動必須存在於流程中。',
        'Begin activity is required.': '開始活動為必填。',
        'End activity is required.': '結束活動為必填。',
        'Begin and End activities must be different.': '開始與結束活動必須不同。',
        'At least one transition is required.': '至少需要一條轉移。',
        'Transitions must connect valid activities.': '轉移必須連接有效活動。',
        'Transitions cannot point to the same activity.': '轉移不可指向同一活動。',
        'Transitions must have a name or condition.': '轉移必須有名稱或條件。',
        'Duplicate transitions are not allowed.': '不允許重複轉移。',
        'All activities must be connected by at least one transition.': '所有活動都必須至少由一條轉移連接。',
        'Begin activity cannot have incoming transitions.': '開始活動不可有入向轉移。',
        'Begin activity must have at least one outgoing transition.': '開始活動必須至少有一條出向轉移。',
        'End activity cannot have outgoing transitions.': '結束活動不可有出向轉移。',
        'End activity must have at least one incoming transition.': '結束活動必須至少有一條入向轉移。',
        'Only one default (empty) transition is allowed per activity.': '每個活動只允許一條預設（空）轉移。',
        'All activities must be reachable from Begin.': '所有活動都必須可從 Begin 到達。',
    },
    Path('goflow/locale/ja/LC_MESSAGES/django.po'): {
        'Workflow Monitor': 'ワークフローモニター',
        'Instances': 'インスタンス',
        'Total': '合計',
        'Running': '実行中',
        'Active': 'アクティブ',
        'Complete': '完了',
        'Workitems': '作業項目',
        'Inactive': '非アクティブ',
        'Blocked': 'ブロック済み',
        'Fallout': '異常',
        'Warned': '警告済み',
        'Breached': '違反',
        'Top Processes': '上位プロセス',
        'Process': 'プロセス',
        'No data': 'データなし',
        'Recent Audit Events': '最近の監査イベント',
        'Time': '時刻',
        'Action': 'アクション',
        'Actor': '実行者',
        'No events': 'イベントなし',
        'Recent Fallout': '最近の異常',
        'Workitem': '作業項目',
        'Activity': 'アクティビティ',
        'Updated': '更新日時',
        'No fallout': '異常なし',
        'Sample Task': 'サンプルタスク',
        'Request #123': '申請 #123',
        'Urgent': '緊急',
        'Needs review': 'レビューが必要',
        'Comment': 'コメント',
        'Approve': '承認',
        'Reject': '却下',
        'process %s disabled.': 'プロセス %s は無効化されています。',
        'completion page.': '完了ページ。',
        'Welcome,': 'ようこそ、',
        'Change password': 'パスワード変更',
        'Log out': 'ログアウト',
        'Log in': 'ログイン',
        'Workflow Designer': 'ワークフローデザイナー',
        'Status': '状態',
        'idle': '待機中',
        'Process Settings': 'プロセス設定',
        'Begin Activity': '開始アクティビティ',
        'End Activity': '終了アクティビティ',
        'Save': '保存',
        'Reload': '再読み込み',
        'Undo': '元に戻す',
        'Redo': 'やり直し',
        'Delete Selected': '選択項目を削除',
        'Shortcuts': 'ショートカット',
        'Ctrl/Cmd+S Save': 'Ctrl/Cmd+S 保存',
        'Ctrl/Cmd+R Reload': 'Ctrl/Cmd+R 再読み込み',
        'Ctrl/Cmd+Z Undo': 'Ctrl/Cmd+Z 元に戻す',
        'Del Delete': 'Del 削除',
        'Activities': 'アクティビティ',
        'Title': 'タイトル',
        'Start': '開始',
        'Kind': '種別',
        'Node Type': 'ノードタイプ',
        'Form Template': 'フォームテンプレート',
        'Form Class': 'フォームクラス',
        'Autostart': '自動開始',
        'Autofinish': '自動完了',
        'Add Activity': 'アクティビティ追加',
        'Transitions': '遷移',
        'From': '開始',
        'To': '終了',
        'Name': '名前',
        'approve': '承認',
        'Condition': '条件',
        'Add Transition': '遷移追加',
        'Canvas': 'キャンバス',
        'Keyboard Shortcuts': 'キーボードショートカット',
        'Ctrl/Cmd + S: Save': 'Ctrl/Cmd + S: 保存',
        'Ctrl/Cmd + R: Reload': 'Ctrl/Cmd + R: 再読み込み',
        'Ctrl/Cmd + Z: Undo': 'Ctrl/Cmd + Z: 元に戻す',
        'Ctrl/Cmd + Y: Redo': 'Ctrl/Cmd + Y: やり直し',
        'Delete/Backspace: Delete selected': 'Delete/Backspace: 選択項目を削除',
        'Double-click node: Rename': 'ノードをダブルクリック: 名前変更',
        'Click edge: Edit label/condition': 'エッジをクリック: ラベル/条件を編集',
        'Close': '閉じる',
        'Validation errors': '検証エラー',
        'Rename activity': 'アクティビティ名を変更',
        'Transition condition or name': '遷移条件または名称',
        'loading': '読み込み中',
        'Reloaded': '再読み込み完了',
        'ready': '準備完了',
        'Reload failed': '再読み込み失敗',
        'error': 'エラー',
        'saving': '保存中',
        'Save failed': '保存失敗',
        'validation error': '検証エラー',
        'Saved': '保存済み',
        'saved': '保存済み',
        'user is not active': 'ユーザーは有効ではありません',
        'authentication failed': '認証に失敗しました',
        'user page.': 'ユーザーページ。',
        'Forbidden': 'アクセス禁止',
        'At least one activity is required.': '少なくとも1つのアクティビティが必要です。',
        'Untitled': '無題',
        'Every activity must have a title.': '各アクティビティにはタイトルが必要です。',
        'Activity titles must be 100 characters or fewer.': 'アクティビティタイトルは100文字以内である必要があります。',
        'Activity kind must be one of: %(choices)s.': 'アクティビティ種別は次のいずれかである必要があります: %(choices)s。',
        'Activity node type must be one of: %(choices)s.': 'アクティビティノードタイプは次のいずれかである必要があります: %(choices)s。',
        'Activity "%(title)s": gateway nodes must use kind=dummy.': 'アクティビティ「%(title)s」: gateway ノードは kind=dummy を使用する必要があります。',
        'Activity "%(title)s": %(node_type)s nodes should enable autostart.': 'アクティビティ「%(title)s」: %(node_type)s ノードでは autostart を有効にすることを推奨します。',
        'Activity "%(title)s": script nodes should enable autofinish.': 'アクティビティ「%(title)s」: script ノードでは autofinish を有効にすることを推奨します。',
        'Activity "%(title)s": notification nodes should not use form_class.': 'アクティビティ「%(title)s」: notification ノードでは form_class を使用しないでください。',
        'Activity titles must be unique.': 'アクティビティタイトルは一意である必要があります。',
        'Begin activity must exist in the workflow.': '開始アクティビティはワークフロー内に存在する必要があります。',
        'End activity must exist in the workflow.': '終了アクティビティはワークフロー内に存在する必要があります。',
        'Begin activity is required.': '開始アクティビティは必須です。',
        'End activity is required.': '終了アクティビティは必須です。',
        'Begin and End activities must be different.': '開始アクティビティと終了アクティビティは異なる必要があります。',
        'At least one transition is required.': '少なくとも1つの遷移が必要です。',
        'Transitions must connect valid activities.': '遷移は有効なアクティビティ同士を接続する必要があります。',
        'Transitions cannot point to the same activity.': '遷移は同一アクティビティを指すことはできません。',
        'Transitions must have a name or condition.': '遷移には名前または条件が必要です。',
        'Duplicate transitions are not allowed.': '重複した遷移は許可されません。',
        'All activities must be connected by at least one transition.': 'すべてのアクティビティは少なくとも1つの遷移で接続されている必要があります。',
        'Begin activity cannot have incoming transitions.': '開始アクティビティに入力遷移は設定できません。',
        'Begin activity must have at least one outgoing transition.': '開始アクティビティには少なくとも1つの出力遷移が必要です。',
        'End activity cannot have outgoing transitions.': '終了アクティビティに出力遷移は設定できません。',
        'End activity must have at least one incoming transition.': '終了アクティビティには少なくとも1つの入力遷移が必要です。',
        'Only one default (empty) transition is allowed per activity.': '各アクティビティでデフォルト（空）の遷移は1つだけ許可されます。',
        'All activities must be reachable from Begin.': 'すべてのアクティビティは Begin から到達可能である必要があります。',
    },
    Path('leavedemo/locale/zh_Hant/LC_MESSAGES/django.po'): {
        'English': '英文',
        'French': '法文',
        'Simplified Chinese': '簡體中文',
        'Traditional Chinese': '繁體中文',
        'Japanese': '日文',
        'Korean': '韓文',
        'German': '德文',
        'Spanish': '西文',
        'Italian': '義大利文',
        'Portuguese': '葡萄牙文',
        'Russian': '俄文',
        'Log in': '登入',
    },
    Path('leavedemo/locale/ja/LC_MESSAGES/django.po'): {
        'English': '英語',
        'French': 'フランス語',
        'Simplified Chinese': '簡体字中国語',
        'Traditional Chinese': '繁体字中国語',
        'Japanese': '日本語',
        'Korean': '韓国語',
        'German': 'ドイツ語',
        'Spanish': 'スペイン語',
        'Italian': 'イタリア語',
        'Portuguese': 'ポルトガル語',
        'Russian': 'ロシア語',
        'Log in': 'ログイン',
    },
    Path('sampleproject/locale/zh_Hant/LC_MESSAGES/django.po'): {
        'English': '英文',
        'French': '法文',
        'Simplified Chinese': '簡體中文',
        'Traditional Chinese': '繁體中文',
        'Japanese': '日文',
        'Korean': '韓文',
        'German': '德文',
        'Spanish': '西文',
        'Italian': '義大利文',
        'Portuguese': '葡萄牙文',
        'Russian': '俄文',
    },
    Path('sampleproject/locale/ja/LC_MESSAGES/django.po'): {
        'English': '英語',
        'French': 'フランス語',
        'Simplified Chinese': '簡体字中国語',
        'Traditional Chinese': '繁体字中国語',
        'Japanese': '日本語',
        'Korean': '韓国語',
        'German': 'ドイツ語',
        'Spanish': 'スペイン語',
        'Italian': 'イタリア語',
        'Portuguese': 'ポルトガル語',
        'Russian': 'ロシア語',
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