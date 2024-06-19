from noa.network_functions.interface.extract.extract_subint import extract_subint
from tests.genr.interface.genr_ifs import genr_ifs


def test_subif(conf):
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
    subint_path = ['.','"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]']
    if_data, subint_args_list = conf('interface', subint_path)
    
    correct_subints = genr_ifs(if_data, issubif=True)
    
    returned_subitn_list = []
    for subints_arg in subint_args_list:
        returned_subitn_list.append((extract_subint(subints_arg)))

    assert returned_subitn_list == correct_subints