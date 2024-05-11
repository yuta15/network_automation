
def merge_subints(interface_subints):
    """
    サブインターフェースの情報を抽出・成形するための関数。
    properties:
        interface_subint: dict
            yang-modelに従ったサブインターフェースdict
    return: dict
        以下の形式で応答
        {
            subint_index1:{},
            subint_index1:{},
            subint_index1:{},
        }
    2025/05/11 subintの情報のみ取得した状態。
    これを加工して必要な情報を取得する。
    現状values()にて取得したデータはリスト型となっている。
    """
    for subint in interface_subints.values():
        print(subint)
        print('-------------------------------------')
        # merge_subint(subint)


def merge_subint(interface_subint):
    """
    単一のサブインターフェースの情報から必要な情報を抽出・成形するための関数。
    properties:
        interface_subint: dict
            単一のサブインターフェースの情報
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
    """
    subinte_index, subint_config, subint_state, subint_ipv4, subint_ipv6 = interface_subint.values()


# def parse_subint_config(subint_config):
    """
    サブインターフェースコンフィグ情報を解析する関数。実装予定
    """


# def parse_subint_state(subint_state)
    """
    サブインターフェースステータス情報を解析する関数。実装予定
    """
# parse_subint_counter(subint_state_counter):
    """
    サブインターフェースカウンタ情報を解析する関数。実装予定
    """


# def parse_subint_ipv4(subint_ipv4):
    """
    サブインターフェースIPv4情報を解析する関数。
    """
# def parse_subint_ipv4_addr(subint_ipv4_addr):
    """
    サブインターフェースIPv4アドレス情報を解析する関数。
    """
# def parse_subint_ipv4_proxy_arp():
    """
    サブインターフェースIPv4 Proxy-arp情報を解析する関数。
    """
# def parse_subint_ipv4_state():
    """
    サブインターフェースステータス情報を解析する関数。
    """
# def parse_subint_ipv4_counter():
    """
    サブインターフェースステータスカウンター情報を解析する関数。
    """
    
    
# def parse_subint_ipv6(subint_ipv6):
    """
    サブインターフェースIPv6情報を解析する関数。
    """
# def parse_subint_ipv6_addr(subint_ipv6_addr):
    """
    サブインターフェースIPv6アドレス情報を解析する関数。
    """
# def parse_subint_ipv6_proxy_arp():
    """
    サブインターフェースIPv6 Proxy-arp情報を解析する関数。
    """
# def parse_subint_ipv6_state():
    """
    サブインターフェースステータス情報を解析する関数。
    """
# def parse_subint_ipv6_counter():
    """
    サブインターフェースステータスカウンター情報を解析する関数。
    """


