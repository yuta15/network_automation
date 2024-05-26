

from noa.network_functions.interface.merge.merge_subint_ipv4 import merge_subint_ipv4


def merge_subint(sub_int_dict) -> dict:
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
                ipv4_dict = merge_subint_ipv4(sub_int_dict.get(sub_int_key))
            # case 'config':
            #     # configの処理を記述
            # case 'state':
            #     # stateの処理を記述
            # case 'openconfig-if-ip:ipv6':
            #     # openconfig-if-ip:ipv6の処理を記述
    return_sub_int_dict[sub_int_index] = config_dict | state_dict | ipv4_dict | ipv6_dict
    return return_sub_int_dict
