

from modules import parse_interface_subinterface


def merge_sub_ints(sub_int_list) -> dict:
    """
    単一のサブインターフェースの情報をマージするための関数。
    args:
        interface_subint: dict
    return: dict
        以下の形式で応答
        {
            subint_index1:{},
            subint_index1:{},
            subint_index1:{},
        }
    remarks:
    """
    return_sub_ints_dict = {}
    sub_int_data_dict = {}
    sub_int_dict = {}
    for sub_int in sub_int_list:
        sub_int_dict = merge_sub_int(sub_int)
        sub_int_data_dict = sub_int_data_dict | sub_int_dict
    return_sub_ints_dict['subinterfaces'] = sub_int_dict
    return return_sub_ints_dict


def merge_sub_int(sub_int_dict) -> dict:
    """
    parse関数にて抽出・成形した単一のサブインターフェースの情報をマージするための関数
    args:
        interface_subint: dict
    return: dict
        index:{
            'enabled': str,
            'admin_status': str,
            'oper_status': str,
            'last_change': str,
            'ip': str,
            'prefix-length': str,
            'discription': str,
        }
    remarks:
        subinterface_config, subinterface_state, subinteraface_ipv6については未実装
    """
    return_sub_int_dict = {}
    config_dict = {}
    state_dict = {}
    ipv4_dict = {}
    ipv6_dict = {}
    sub_int_index = ""
    sub_int_keys = ['index', 'config', 'state', 'openconfig-if-ip:ipv4', 'openconfig-if-ip:ipv6']
    for sub_int_key in sub_int_keys:
        match sub_int_key:
            case 'index':
                sub_int_index = sub_int_dict.get(sub_int_key)
            case 'openconfig-if-ip:ipv4':
                ipv4_dict = merge_sub_int_ipv4(sub_int_dict.get(sub_int_key))
            # case 'config':
            #     # configの処理を記述
            # case 'state':
            #     # stateの処理を記述
            # case 'openconfig-if-ip:ipv6':
            #     # openconfig-if-ip:ipv6の処理を記述
    return_sub_int_dict[sub_int_index] = config_dict | state_dict | ipv4_dict | ipv6_dict
    return return_sub_int_dict


def merge_sub_int_ipv4(sub_int_ipv4_dict) -> dict:
    """
    サブインターフェースIPv4情報を解析する関数。
    properties:
        sub_int_ipv4_dict: dict
    return:
        return_sub_int_ipv4: dict
        {
            ip:
            prefix-length
            *proxy-arp
            *state
        }
        *未実装
    """
    return_sub_int_ipv4_dict = {}
    addresses_dict = {}
    proxy_arp_dict = {}
    state_dict = {}
    ipv4_keys = ['addresses', 'proxy-arp', 'state']
    for ipv4_key in ipv4_keys:
        match ipv4_key:
            case 'addresses':
                addresses_dict = parse_interface_subinterface.parse_subint_ipv4_addr(sub_int_ipv4_dict.get(ipv4_key))                
            # case 'proxy-arp':
                # proxy-arp処理
            # case 'state':
                # state処理
    return_sub_int_ipv4_dict = addresses_dict | proxy_arp_dict | state_dict
    return return_sub_int_ipv4_dict

