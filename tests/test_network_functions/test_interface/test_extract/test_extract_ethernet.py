import jmespath
import json
import os

from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet


def test_merge_ethernet():
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
    json_path = os.getcwd() + '/example_interface.json'
    with open(json_path, mode='r') as f:
        base_data = json.loads(f.read())
    
    eth_path = '"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"'
    eth_arg_list = jmespath.search(eth_path, base_data)
    
    mac_addr = 'mac-address'
    auto_nego = 'auto-negotiate'
    port_speed = 'port-speed'
    duplex = 'negotiated-duplex-mode'
    keys = [mac_addr, auto_nego, port_speed, duplex]
    
    correct_path = f'{eth_path}.state.["{mac_addr}", "{auto_nego}", "{port_speed}", "{duplex}"]'
    correct_data_list = jmespath.search(correct_path,base_data)
    correct_dict_list = [dict(zip(keys, corrent_val)) for corrent_val in correct_data_list]
    returned_eth_list = []
    
    for eth in eth_arg_list:
        returned_eth_list.append(extract_ethernet(eth))

    assert returned_eth_list == correct_dict_list