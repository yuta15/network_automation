import jmespath

from noa.network_functions.interface.interface import interface
from tests.mods.interface.correct_eth_data import correct_eth_data
from tests.mods.interface.correct_state_data import correct_state_data
from tests.mods.interface.correct_subint_data import correct_subint_data


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
    eth_path = '"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"'
    state_path = '"openconfig-interfaces:interfaces".interface[*].state'
    subint_path = '"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]'
    paths = [int_arg_path, int_name_path, eth_path, state_path, subint_path]
    int_args, int_names, eth_arg_list, state_arg_list, subint_args_list = conf(paths)

    print(eth_arg_list)
    correct_states = correct_state_data(state_arg_list)
    correct_eths = correct_eth_data(eth_arg_list)
    correct_subints = correct_subint_data(subint_args_list)
    
    key_state = 'state'
    key_eth = 'ethernet'
    key_subints = 'subinterfaces'
    
    datas = []
    for state, eth, subint in zip(correct_states, correct_eths, correct_subints):
        state_d = {key_state: state}
        eth_d = {key_eth: eth}
        subint_d = {key_subints: subint}
        datas.append(state_d | eth_d | subint_d)

    returned_int_data = []
    correct_int_data = []
    assert returned_int_data == correct_int_data
    
    
    
    
