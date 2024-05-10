import copy
import json

from modules import get_data


def generate_all_interface_data(interface_dict):
    """
    class Hostにて取得したinterfaceデータをもとに応答するデータを生成する関数。
    必要なデータを生成する。
    interface情報は
    **args: obj
    →
    return: obj
    interface_name:{
        'ethernet':{
            'mac-address':,
            'duplex':,
            'speed':
        },
        subinterface_index:{
            'enabled': ,
            'admin_status':,
            'oper_status':,
            'last_change':,
            'ip':,
            'prefix-length':,
            'discription':,
        },
    }
    """
    # print(type(interface_obj))
    # アンパッキングして各情報を分離
    interface_name, interface_config, interface_state, interface_subinterface, interface_ethernet = interface_dict.values()
    generate_interface_subinterface(interface_subinterface)



def generate_interface_subinterface(subinterface_dict):
    """
    2025/05/11 subinterfaceの情報のみ取得した状態。
    これを加工して必要な情報を取得する。
    現状values()にて取得したデータはリスト型となっている。
    """
    for subinterface in subinterface_dict.values():
        print (type(subinterface))
        print ('-----------------------------------------------------------------')
    









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


