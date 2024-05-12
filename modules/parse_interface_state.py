def parse_int_state(int_state_dict):
    """
    インターフェースステータス情報をマージするための関数
    args:
        int_state_dict: dict
    return:
        return_int_state_dict: dict
        {
            enabled:
            admin-status:
            oper-status:
            last-change:
        }        
    remarks:
    """
    required_state_keys = ['enabled', 'admin-status', 'oper-status', 'last-change']
    return_int_state_dict = {}
    for state_key in required_state_keys:
        return_int_state_dict[state_key] = int_state_dict.get(state_key)
    return return_int_state_dict