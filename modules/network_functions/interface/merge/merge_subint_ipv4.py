

from modules.network_functions.interface.parsers.parse_subint_ipv4_addr import parse_subint_ipv4_addr


def merge_subint_ipv4(sub_int_ipv4_dict) -> dict:
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
                addresses_dict = parse_subint_ipv4_addr(sub_int_ipv4_dict.get(ipv4_key))
            # case 'proxy-arp':
                # proxy-arp処理
            # case 'state':
                # state処理
    return_sub_int_ipv4_dict = addresses_dict | proxy_arp_dict | state_dict
    return return_sub_int_ipv4_dict

