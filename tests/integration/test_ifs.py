from noa.network_functions.interface.interfaces import interfaces
from tests.genr.genr_ifs import genr_ifs

def test_ifs(conf):
    """
    interfaces関数の統合テスト用関数
    """
    arg_path = ['.', '"openconfig-interfaces:interfaces"."interface"', ]
    if_data, arg_data = conf(arg_path)
    cor_data = genr_ifs(if_data)
    returned_data = interfaces(arg_data)
    
    assert returned_data == cor_data
