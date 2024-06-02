import jmespath

from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet


def test_extract_ethernet(conf):
    """
    extract_ethernetテスト用関数
    example_interface.jsonから必要な情報を抽出し、返り値が想定通りであることを確認する。
    {
        "mac-address",
        "auto-negotiate",
        "port-speed",
        "negotiated-duplex-mode"
    }
    """
    eth_path = '"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"'
    eth_arg_list = conf(eth_path)
    
    mac_addr = 'mac-address'
    auto_nego = 'auto-negotiate'
    port_speed = 'port-speed'
    duplex = 'negotiated-duplex-mode'
    keys = [mac_addr, auto_nego, port_speed, duplex]
    
    correct_path = f'[*].state.["{mac_addr}", "{auto_nego}", "{port_speed}", "{duplex}"]'
    correct_data_list = jmespath.search(correct_path,eth_arg_list)
    correct_dict_list = [dict(zip(keys, corrent_val)) for corrent_val in correct_data_list]
    returned_eth_list = []
    
    for eth in eth_arg_list:
        returned_eth_list.append(extract_ethernet(eth))

    print(extract_ethernet('a'))
    assert returned_eth_list == correct_dict_list