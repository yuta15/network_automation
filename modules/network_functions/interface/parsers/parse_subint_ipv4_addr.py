


def parse_subint_ipv4_addr(sub_int_ipv4_addr_dict) -> dict:
    """
    サブインターフェースのIPv4アドレスステート情報を解析する関数。
    args:
        subint_ipv4_addr: dict
    return:
        {
            'ip': None or str or list,
            'prefix-length': None or str or list,
        }
    """
    state, ip, prefix_len = 'state', 'ip', 'prefix-length'
    return_ipv4_data = {'ip': None, 'prefix-length': None,}
    if sub_int_ipv4_addr_dict is None:
        return return_ipv4_data
    elif len(sub_int_ipv4_addr_dict.get('address')) == 1:
        ipv4_add = sub_int_ipv4_addr_dict.get('address')[0]
        return_ipv4_data['ip'] = ipv4_add[state].get(ip)
        return_ipv4_data['prefix-length'] = ipv4_add[state].get(prefix_len)
        return return_ipv4_data
    else:
        ip_list = []
        prefix_len_list = []
        for address_dict in sub_int_ipv4_addr_dict.get('address'):
            ip_list.append(address_dict[state][ip])
            prefix_len_list.append(address_dict[state][prefix_len])
        return_ipv4_data['ip'] = ip_list
        return_ipv4_data['prefix-length'] = prefix_len_list
        return return_ipv4_data
    