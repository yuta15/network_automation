import jmespath

def genr_state(state_data):
    """
    正しいstateデータを生成する関数
    args:
        state_data: list
          - subinterface配下のリスト
    returned:
        correct_datas: list
          - stateの正解データのリスト
    """
    
    enabled = 'enabled'
    admin_status = '"admin-status"'
    oper_status = '"oper-status"'
    last_change = '"last-change"'
    state_path = f'[*].{{enabled: {enabled}, "admin-status": {admin_status}, "oper-status": {oper_status}, "last-change": {last_change}}}'
    correct_datas = jmespath.search(state_path, state_data)
    return correct_datas