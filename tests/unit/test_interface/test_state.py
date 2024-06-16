from noa.network_functions.interface.extract.extract_state import extract_state
from tests.genr.genr_ifs import genr_ifs

def test_state(conf):
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
    state_path = ['.', '"openconfig-interfaces:interfaces".interface[*].state']
    if_data, state_arg_list = conf(state_path)
    
    correct_datas = genr_ifs(if_data, isstate=True)
    
    returned_state_list = []
    for state_data in state_arg_list:
        returned_state_list.append(extract_state(state_data))
    
    assert returned_state_list == correct_datas