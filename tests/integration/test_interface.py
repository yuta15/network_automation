from noa.network_functions.interface.interface import interface
from tests.mods.interface.generate_test_data_eth import generate_test_data_eth
from tests.mods.interface.generate_test_data_state import generate_test_data_state
from tests.mods.interface.generate_test_data_subint import generate_test_data_subint


def test_interface(conf):
    """
    interfaceをテストする関数
        return: dict
    {
        interface_name:{
            'state': {}
            'ethernet':{},
            'subinterfaces': {}
        }
    }
    """
    int_arg_path = '"openconfig-interfaces:interfaces".interface'
    int_name_path = '"openconfig-interfaces:interfaces".interface[*].name'
    eth_path = '"openconfig-interfaces:interfaces".interface[*]'
    state_path = '"openconfig-interfaces:interfaces".interface[*].state'
    subint_path = '"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]'
    
    paths = [int_arg_path, int_name_path, eth_path, state_path, subint_path]
    int_args, int_names, eth_arg_list, state_arg_list, subint_args_list = conf(paths)
    
    state_data = generate_test_data_state(state_arg_list)
    eth_data = generate_test_data_eth(eth_arg_list)
    subint_data = [generate_test_data_subint(subint) for subint in subint_args_list]

    ethernet_key = 'ethernet'
    state_key = 'state'
    subint_key = 'subinterfaces'

    correct_int_data = []
    returned_int_data = []
    
    for int_name, state, eth, subint in zip(int_names, state_data, eth_data, subint_data):
        int_dict = {}
        state_dict = {}
        eth_dict = {}
        subint_dict = {}
        eth_dict[ethernet_key] = eth
        state_dict[state_key] = state
        subint_dict[subint_key] = subint
        
        int_dict[int_name] = state_dict | eth_dict | subint_dict
        correct_int_data.append(int_dict)

    for int_arg in int_args:
        returned_int_data.append(interface(int_arg))
        
    assert returned_int_data == correct_int_data