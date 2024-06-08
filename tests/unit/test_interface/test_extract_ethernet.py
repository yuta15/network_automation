
from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet
from tests.mods.interface.correct_eth_data import correct_eth_data


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
    eth_path = ['"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"']
    eth_arg_list = conf(eth_path)[0]
    
    correct_dict_list = correct_eth_data(eth_arg_list)
    returned_eth_list = []
    
    for eth in eth_arg_list:
        returned_eth_list.append(extract_ethernet(eth))

    assert returned_eth_list == correct_dict_list