import jmespath


def correct_eth_data(eth_arg_list):
    """
    テストの正解データを生成する。
    """
    key_mac_addr = 'mac-address'
    key_auto_nego = 'auto-negotiate'
    key_port_speed = 'port-speed'
    key_duplex = 'negotiated-duplex-mode'
    keys = [key_mac_addr, key_auto_nego, key_port_speed, key_duplex]
    
    correct_path = f'[*].state.["{key_mac_addr}", "{key_auto_nego}", "{key_port_speed}", "{key_duplex}"]'
    correct_data_list = jmespath.search(correct_path,eth_arg_list)
    correct_dict_list = [dict(zip(keys, correct_val)) for correct_val in correct_data_list]

    return correct_dict_list