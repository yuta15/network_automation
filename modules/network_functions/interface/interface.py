

from modules.network_functions.interface.merge.merge_all_subint import merge_all_subint
from modules.network_functions.interface.merge.merge_ethernet import merge_ethernet
from modules.network_functions.interface.merge.merge_state import merge_state


def interface(interface_dict):
    """
    単一のインターフェースのethernet, subinterface, config, state情報をマージする関数
    args: 
        interface_dict: dict
    return: dict
        interface_name:{
            'ethernet':{},
            'subinterfaces': {}
        }
    remarks:
        config, state, ethernet情報については未実装
    """
    interface_name = ""
    return_interface_dict = {}
    ethernet_dict = {}
    sub_int_dict = {}
    config_dict = {}
    state_dict = {}
    interface_keys = ['name', 'config', 'state', 'subinterfaces', 'openconfig-if-ethernet:ethernet']
    for interface_key in interface_keys:
        match interface_key:
            case 'name':
                interface_name = interface_dict.get(interface_key)
            case 'subinterfaces':
                data_dict = interface_dict.get(interface_key)
                sub_int_dict = merge_all_subint(data_dict.get('subinterface'))
            case 'openconfig-if-ethernet:ethernet':
                data_dict = interface_dict.get(interface_key)
                ethernet_dict = merge_ethernet(data_dict)
            case 'state':
                data_dict = interface_dict.get(interface_key)
                state_dict = merge_state(data_dict)
            # case 'config':
                # config用のコードを記載
    return_interface_dict[interface_name] =  state_dict | ethernet_dict | sub_int_dict | config_dict 
    return return_interface_dict

