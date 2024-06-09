import jmespath

from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet
from noa.network_functions.interface.extract.extract_subint import extract_subint
from noa.network_functions.interface.extract.extract_state import extract_state

def interface(interface_dict):
    """
    単一のインターフェースのethernet, subinterface, config, state情報をマージする関数
    args: 
        interface_dict: dict
    return: dict
        interface_name:{
            'state': {}
            'ethernet':{},
            'subinterfaces': {}
        }
    remarks:
        config情報については未実装
    """
    
    state_dict = {
        "enabled": None,
        "admin-status": None,
        "oper-status": None,
        "last-change": None 
    }
    ethernet_dict = {
        "mac-address": None,
        "auto-negotiate": None,
        "port-speed": None,
        "negotiated-duplex-mode": None
    }
    sub_int_dict ={
        '0':{
            'enabled': None,
            'admin-status': None,
            'oper-status': None,
            'last-change': None,
            'ip': None,
            'prefix-length': None,
            'description': None,
        }
    }
    
    return_interface_dict = {}
    
    interface_keys = [key for key in interface_dict.keys()]
    for interface_key in interface_keys:
        match interface_key:
            case 'name':
                interface_name = interface_dict.get(interface_key)
            case 'subinterfaces':
                data_dict = interface_dict.get(interface_key)
                sub_int_dict = extract_subint(data_dict.get('subinterface'))
            case 'openconfig-if-ethernet:ethernet':
                data_dict = interface_dict.get(interface_key)
                ethernet_dict = extract_ethernet(data_dict)
            case 'state':
                data_dict = interface_dict.get(interface_key)
                state_dict = extract_state(data_dict)
            # case 'config':
                # config用のコードを記載
    
    states = {'state': state_dict}
    eth = {'ethernet': ethernet_dict}
    subint = {'subinterfaces': sub_int_dict}
    
    return_interface_dict[interface_name] =  states | eth | subint

    return return_interface_dict

