

from modules.network_functions.interface.parsers.parse_ethernet import parse_ethernet


def merge_ethernet(ethernet_dict):
    """
    ethernet情報をマージする関数
    args:
        ethernet_dict: dict or None
    return:
        return_ethernet_dict
        {
            'mac-address':
            'auto-negotiate':
            'port-speed':
            'negotiated-duplex-mode'
            *config情報が必要になれば以下に追加
        }
    remarks
        現状、ethernetからは上記のみが必要な情報となり、
        cofnig内の情報は特に必要ない状態。
        modelの変更への拡張性のため、parse_ethernetを呼びだすのみとする。
    """
    return_ethernet_dict = {}
    ethernet_state_dict = {}
    ethernet_config_dict = {}
    if ethernet_dict == None:
        return_ethernet_dict.update([('mac-address', None), ('auto-negotiate', None), ('port-speed', None),('negotiated-duplex-mode', None)])
        return return_ethernet_dict

    for ethernet_key in ethernet_dict.keys():
        match ethernet_key:
            case 'state':
                ethernet_data = ethernet_dict.get(ethernet_key)
                ethernet_state_dict = parse_ethernet(ethernet_data)
            # case 'config':
            #     ethernet_config_dict = parse_ethernet.parse_ethernet_config(ethernet_key)

    return_ethernet_dict = ethernet_config_dict | ethernet_state_dict
    return return_ethernet_dict