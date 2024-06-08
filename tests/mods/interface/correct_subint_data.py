import jmespath


def correct_subint_data(subint_args_list):
    key_enbaled = 'enabled'
    key_admin_status = 'admin-status'
    key_oper_status = 'oper-status'
    key_last_change = 'last-change'
    key_description = 'description'
    key_ip = 'ip'
    key_prefix_length = 'prefix-length'

    subint_state_keys = [key_enbaled, key_admin_status, key_oper_status, key_last_change]
    subint_config_keys = [key_description]
    subint_addresses_keys = [key_ip, key_prefix_length]

    correct_subint_list = []
    
    for subints_arg in subint_args_list:
        indexes = jmespath.search('[*].index', subints_arg)
        subint_states = jmespath.search(f'[*].state.["{key_enbaled}", "{key_admin_status}", "{key_oper_status}", "{key_last_change}"]', subints_arg)
        base_subint_addresses = [jmespath.search(f'"openconfig-if-ip:ipv4".addresses.address[*].state.["{key_ip}", "{key_prefix_length}"][]', subint) for subint in subints_arg]
        subint_addresses = [[None, None] if int_data == None else int_data for int_data in base_subint_addresses]
        subint_configs = jmespath.search(f'[*].config.["{key_description}"]', subints_arg)
        subint_state_dict_list = [dict(zip(subint_state_keys, subint_state_val)) for subint_state_val in subint_states]
        subint_addresses_dict_list = [dict(zip(subint_addresses_keys, subint_address_val)) for subint_address_val in subint_addresses]
        subint_config_dict_list = [dict(zip(subint_config_keys, subint_config_val)) for subint_config_val in subint_configs]
        correct_subint = dict(zip(indexes, [dict(subint_state | subint_address | subint_config) for subint_state, subint_address, subint_config in zip(subint_state_dict_list, subint_addresses_dict_list, subint_config_dict_list)]))
        correct_subint_list.append(correct_subint)
        
    return correct_subint_list