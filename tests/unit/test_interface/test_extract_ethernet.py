import jmespath

from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet
from tests.mods.interface.generate_test_data_eth import generate_test_data_eth


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
    eth_path = [
        '"openconfig-interfaces:interfaces".interface[*]',
        '"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"'
        ]
    correct_eth_data = conf(eth_path)[0]
    args_eth_data = conf(eth_path)[1]
    eth_datas = [ eth_data for eth_data in correct_eth_data if "openconfig-if-ethernet:ethernet" in eth_data ]
    correct_datas = generate_test_data_eth(eth_datas)
    returned_eth_list = []
    for eth in args_eth_data:
        returned_eth_list.append(extract_ethernet(eth))

    assert returned_eth_list == correct_datas