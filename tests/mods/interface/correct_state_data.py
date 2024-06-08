import jmespath


def correct_state_data(state_arg_list):
    """
    正解のデータを生成する関数。
    args:
        state_arg_list: list
        openconfig-if-ethernet:ethernet
    """
    key_enabled = 'enabled'
    key_admin_status = 'admin-status'
    key_oper_status = 'oper-status'
    key_last_change = 'last-change'
    keys = [key_enabled, key_admin_status, key_oper_status, key_last_change]
    
    correct_data_path = f'[*].["{key_enabled}","{key_admin_status}","{key_oper_status}","{key_last_change}"]'
    correct_data_list = jmespath.search(correct_data_path, state_arg_list)
    correct_dict_list = [dict(zip(keys, correct_val)) for correct_val in correct_data_list]
    
    return correct_dict_list