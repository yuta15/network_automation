import os
import json
import jmespath

from noa.network_functions.interface.extract.extract_state import extract_state


def test_extract_state(conf):
    '''
    extract_state関数をテストするための関数
    example_interface.jsonから必要な情報を抽出し、返り値が想定通りであることを確認する。
    returned:
    {
        enabled:
        admin-status:
        oper-status:
        last-change:
    }
    '''
    state_path = '"openconfig-interfaces:interfaces".interface[*].state'
    state_arg_list = conf(state_path)

    enabled = 'enabled'
    admin_status = 'admin-status'
    oper_status = 'oper-status'
    last_change = 'last-change'
    keys = [enabled, admin_status, oper_status, last_change]
    
    correct_data_path = f'[*].["{enabled}","{admin_status}","{oper_status}","{last_change}"]'
    correct_data_list = jmespath.search(correct_data_path, state_arg_list)
    correct_dict_list = [dict(zip(keys, correct_val)) for correct_val in correct_data_list]
    
    returned_state_list = []
    for state_data in state_arg_list:
        returned_state_list.append(extract_state(state_data))
    
    assert returned_state_list == correct_dict_list
    print(extract_state([]))