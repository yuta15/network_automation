import jmespath


def extract_subint(subints: list) -> dict:
    """
    引数で受け取ったデータから情報を抽出するための関数
    
    :arg state_dict: list
        state内のdict
    
    :returns return_subints_data: dict
        state内のdictから必要な情報を抽出したもの
        {
            index:{
                'enabled': str,
                'admin-status': str,
                'oper-status': str,
                'last-change': str,
                'ip': str,
                'prefix-length': str,
                'description': str,
            }
        }
    """
    enabled_path = 'state.enabled'
    admin_status_path = 'state."admin-status"'
    oper_status_path = 'state."oper-status"'
    last_change_path = 'state."last-change"'
    ip_path = '"openconfig-if-ip:ipv4".addresses.address[].state.ip'
    prefix_length_path = '"openconfig-if-ip:ipv4".addresses.address[].state."prefix-length"'
    description_path = 'config.description'
    
    data_paths = f'[].{{enabled: {enabled_path},"admin-status": {admin_status_path}, "oper-status": {oper_status_path}, "last-change": {last_change_path}, ip: {ip_path}, "prefix-length": {prefix_length_path}, description: {description_path}}}[]'
    index_path = '[].index[]'
    subint_data = jmespath.search(data_paths, subints)
    index_data = jmespath.search(index_path, subints)

    return_subints_data = {}
    for index, subint in zip(index_data, subint_data):
        return_subints_data[index] = subint
    return return_subints_data
