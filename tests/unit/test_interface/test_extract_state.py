from noa.network_functions.interface.extract.extract_state import extract_state
from tests.mods.interface.correct_state_data import correct_state_data

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
    state_path = ['"openconfig-interfaces:interfaces".interface[*].state']
    state_arg_list = conf(state_path)[0]

    correct_dict_list = correct_state_data(state_arg_list)
    
    returned_state_list = []
    for state_data in state_arg_list:
        returned_state_list.append(extract_state(state_data))
    
    assert returned_state_list == correct_dict_list
    print(extract_state([]))