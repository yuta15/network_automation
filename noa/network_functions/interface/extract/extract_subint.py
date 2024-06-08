import jmespath


def extract_subint(subints: list) -> list:
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
    key_enable = 'enabled'
    key_admin_status = 'admin-status'
    key_oper_status = 'oper-status'
    key_last_change = 'last-change'
    key_ip = 'ip'
    key_prefix_length = 'prefix-length'
    key_description = 'description'
    state_keys = [key_enable, key_admin_status, key_oper_status, key_last_change]
    ip_keys = [key_ip, key_prefix_length]
    config_keys = [key_description]
    
    base_path = '[*]'
    index_path = f'{base_path}.index'
    state_path = f'{base_path}.state.["{key_enable}", "{key_admin_status}", "{key_oper_status}", "{key_last_change}"]'
    ip_path = f'"openconfig-if-ip:ipv4".addresses.address[*].state.["{key_ip}", "{key_prefix_length}"][]'
    confi_path = f'{base_path}.config.["{key_description}"]'
    
    index_datas = jmespath.search(index_path, subints)
    state_datas = jmespath.search(state_path, subints)
    base_ip_datas = [jmespath.search(ip_path, subint) for subint in subints]
    ip_datas = [[None,None] if ip_data == None else ip_data for ip_data in base_ip_datas]
    confi_datas = jmespath.search(confi_path, subints)
    
    states = [dict(zip(state_keys, state_val)) for state_val in state_datas]
    ips = [dict(zip(ip_keys, ip_val)) for ip_val in ip_datas]
    configs = [dict(zip(config_keys, config_val)) for config_val in confi_datas]
    return_subints_data = dict(zip(index_datas, [dict(state | ip | config) for state, ip, config in zip(states, ips, configs)]))

    return return_subints_data