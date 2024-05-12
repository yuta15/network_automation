

from modules import merge_interface_ethernet, merge_interface_subinterface, parse_interface_state


def merge_interfaces(all_interface_list):
    """
    複数のインターフェースの情報をマージする関数
    args:
        all_interface_dict: dict
            すべてのインターフェース情報
    return: dict
        {
            interfase_name1:{}
            interfase_name2:{}
            interfase_name3:{}
        }
    remarks:
    """
    return_all_interfaces = {}
    for interface_dict in all_interface_list:
        return_all_interfaces = return_all_interfaces | merge_interface(interface_dict)
    return return_all_interfaces


def merge_interface(interface_dict):
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
                sub_int_dict = merge_interface_subinterface.merge_sub_ints(data_dict.get('subinterface'))
            case 'openconfig-if-ethernet:ethernet':
                data_dict = interface_dict.get(interface_key)
                ethernet_dict = merge_interface_ethernet.merge_ethernet(data_dict)
            case 'state':
                data_dict = interface_dict.get(interface_key)
                state_dict = parse_interface_state.parse_int_state(data_dict)
            # case 'config':
                # config用のコードを記載
    return_interface_dict[interface_name] =  state_dict | ethernet_dict | sub_int_dict | config_dict 
    return return_interface_dict

