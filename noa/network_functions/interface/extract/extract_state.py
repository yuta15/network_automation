import jmespath
from jmespath.exceptions import JMESPathTypeError


def extract_state(state_dict: dict) -> dict:
    """
    引数で受け取ったデータから情報を抽出するための関数
    
    :arg state_dict: dict
        state内のdict
    
    :returns return_state_dict: dict
        state内のdictから必要な情報を抽出したもの
        {
            "enabled": str,
            "admin-status": str,
            "oper-status": str,
            "last-change": str 
        }
    """
    enabled = 'enabled'
    admin_status = 'admin-status'
    oper_status = 'oper-status'
    last_change = 'last-change'
    keys = [enabled, admin_status, oper_status, last_change]
    dict_path = f'["{enabled}", "{admin_status}", "{oper_status}", "{last_change}"]'
    
    state_datas = jmespath.search(dict_path, state_dict)
    if state_datas is None:
        state_datas = [None] * len(keys)

    return_state_dict = dict(zip(keys, state_datas))
    return return_state_dict