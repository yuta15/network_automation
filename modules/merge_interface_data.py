import copy

from modules import merge_subinterfaces


def generate_all_interface_data(all_interface_list):
    """
    引数で渡された全インターフェース情報から必要な情報を応答する関数。
    
    properties:
        all_interface_dict: dict
            すべてのインターフェース情報
    return: dict
        インターフェース情報

    remarks:

    """
    return_all_interfaces = {}
    for interface_dict in all_interface_list:
        merge_interface_data(interface_dict)



def merge_interface_data(interface_dict):
    """
    引数で渡された単一のインターフェース情報から必要な情報を応答する関数。

    properties: 
        interface_dict: dict
            単一のインターフェース情報
        return: dict
            interface_name:{
                
                'ethernet':{},
                'subinterfaces': [{}]
        }
    """
    interface_name, interface_config, interface_state, interface_subinterface, interface_ethernet = interface_dict.values()
    merge_subinterfaces.merge_subints(interface_subinterface)
    # merge_ethernet(interface_ethernet)
    






def extraction_interface_ethernet(interface_ethernet):
    """
    インターフェース情報からethernet情報を抽出・整形するための関数。
    properties:
        interface_ethernet: dict
    return:
        {
            'mac-address': str,
            'duplex': str,
            'speed': str
        },
    """


# def parse_dict_keys(parse_dict):
    




def generate_return_data(return_json):
    interfaces_json = return_json["openconfig-interfaces:interfaces"]['interface']
    interface_informations = {}
    interface_data_base = {}
    subinterface_data_base = {
            "subinterface_is_enabled": "",
            "subinterface_admin_status": "",
            "subinterface_oper_status": "",
            "subinterface_last_change": "",
            "subinterface_address": "",
            "subinterface_prefix": "",
            "subinterface_description": ""
    }

    for interface in interfaces_json:
        interface_data = copy.deepcopy(interface_data_base)
                
        for subinterface in interface['subinterfaces']['subinterface']:
            subinterface_data = copy.deepcopy(subinterface_data_base)
            subinterface_index = subinterface['index']
            subinterface_data['subinterface_is_enabled'] = subinterface['config']['enabled']
            subinterface_data['subinterface_admin_status'] = subinterface['state']['admin-status']
            subinterface_data['subinterface_oper_status'] =  subinterface['state']['oper-status']
            subinterface_data['subinterface_last_change'] =  subinterface['state']['last-change']
            
            if 'addresses' in subinterface['openconfig-if-ip:ipv4']:
                subinterface_data['subinterface_address'] = subinterface['openconfig-if-ip:ipv4']['addresses']['address'][0]['config']['ip']
                subinterface_data['subinterface_prefix'] =  subinterface['openconfig-if-ip:ipv4']['addresses']['address'][0]['config']['prefix-length']
                
            elif 'description' in subinterface['config']:
                subinterface_data['subinterface_description'] = subinterface['config']['description']
                
            else:
                subinterface_data['subinterface_description'] = None
                subinterface_data['subinterface_address'] = None
                subinterface_data['subinterface_prefix'] = None
                
            interface_data[subinterface_index] = subinterface_data
        interface_informations[interface['name']] = interface_data
    return interface_informations


