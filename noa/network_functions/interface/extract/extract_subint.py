import jmespath


def extract_subint(state_dict: dict) -> dict:
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