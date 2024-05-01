import copy
import json

from modules import get_data

def get_interface_all():
    USER = "cisco"
    PASS = "cisco"
    host = "172.18.1.2"
    get_headers = {'Accept': 'application/yang-data+json'}
    base_api_url = f"https://{host}/restconf/data/openconfig-interfaces:interfaces"    
    data = get_data.get_interface_data(USER, PASS, get_headers, base_api_url)    
    interface_data = json.dumps(generate_return_data(data))
    print(type(interface_data))
    return interface_data


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