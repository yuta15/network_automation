from noa.network_functions.interface.extract.extract_subint import extract_subint
from tests.mods.interface.generate_test_data_subint import generate_test_data_subint


def test_extract_subint(conf):
    '''
    extract_state関数をテストするための関数
    example_interface.jsonから必要な情報を抽出し、返り値が想定通りであることを確認する。
    returned:
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
    '''
    subint_path = ['"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]']
    subint_args_list = conf(subint_path)[0]
    
    correct_subints = [generate_test_data_subint(subint_arg) for subint_arg in subint_args_list]
    returned_subitn_list = []

    for subints_arg in subint_args_list:
        returned_subitn_list.append((extract_subint(subints_arg)))

    assert returned_subitn_list == correct_subints