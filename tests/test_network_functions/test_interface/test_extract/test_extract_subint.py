import os
import json
import jmespath

from noa.network_functions.interface.extract.extract_subint import extract_subint


def test_extract_subint():
    '''
    extract_state関数をテストするための関数
    example_interface.jsonから必要な情報を抽出し、返り値が想定通りであることを確認する。
    returned:
    {
        index:{
            'enabled': str,
            'admin_status': str,
            'oper_status': str,
            'last_change': str,
            'ip': str,
            'prefix-length': str,
            'discription': str,
        }
    }
    '''
    json_path = os.getcwd() + '/example_interface.json'
    with open(json_path, mode='r') as f:
        base_data = json.loads(f.read())
    
    subint_path = '"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]'
    subint_args_list = jmespath.search(subint_path, base_data)
    
    enbaled = 'enabled'
    admin_status = 'admin-status'
    oper_status = 'oper-status'
    last_change = 'last-change'
    description = 'description'
    ip = 'ip'
    prefix_length = 'prefix-length'
    
    subint_state_keys = [enbaled, admin_status, oper_status, last_change]
    subint_config_keys = [description]
    subint_addresses_keys = [ip, prefix_length]
    
    correct_subint_list = []
    returned_subitn_list = []
    
    for subint_arg in subint_args_list:
        indexes = jmespath.search('[*].index', subint_arg)
        subint_states = jmespath.search(f'[*].state.["{enbaled}", "{admin_status}", "{oper_status}", "{last_change}"]', subint_arg)
        subint_addresses = jmespath.search(f'[*]."openconfig-if-ip:ipv4".addresses.address[*].state.["{ip}", "{prefix_length}"][]', subint_arg)
        if subint_addresses == []:
            subint_addresses.append([None, None])
        subint_configs = jmespath.search(f'[*].config.["{description}"]', subint_arg)
        subint_state_dict_list = [dict(zip(subint_state_keys, subint_state_val)) for subint_state_val in subint_states]
        subint_addresses_dict_list = [dict(zip(subint_addresses_keys, subint_address_val)) for subint_address_val in subint_addresses]
        subint_config_dict_list = [dict(zip(subint_config_keys, subint_config_val)) for subint_config_val in subint_configs]
        correct_subint = dict(zip(indexes, [dict(subint_state | subint_address | subint_config) for subint_state, subint_address, subint_config in zip(subint_state_dict_list, subint_addresses_dict_list, subint_config_dict_list)]))
        correct_subint_list.append(correct_subint)
        
        returned_subitn_list.append((extract_subint(subint_arg)))
        
    assert returned_subitn_list == correct_subint_list