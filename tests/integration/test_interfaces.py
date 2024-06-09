import jmespath

from noa.network_functions.interface.interfaces import interfaces
from tests.mods.interface.generate_test_data_eth import generate_test_data_eth
from tests.mods.interface.generate_test_data_state import generate_test_data_state
from tests.mods.interface.generate_test_data_subint import generate_test_data_subint

def test_interfaces(conf):
    """
    interfaces関数の統合テスト用関数
    """
    arg_path = ['"openconfig-interfaces:interfaces"."interface"']
    arg_data = conf(arg_path)[0]
    
    
    
    returned_data = interfaces(arg_data)
    
    