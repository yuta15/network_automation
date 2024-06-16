import jmespath

from noa.network_functions.interface.extract.extract_ethernet import extract_ethernet
from tests.genr.genr_ifs import genr_ifs


def test_eth(conf):
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
        '.',
        '"openconfig-interfaces:interfaces".interface[*]."openconfig-if-ethernet:ethernet"'
        ]
    if_data, args_eth_data = conf(eth_path)
    cor_datas = genr_ifs(if_data, iseth=True)
    del_data = {'mac-address': None, 'auto-negotiate': None, 'port-speed': None, 'negotiated-duplex-mode': None}
    cor_datas = [data for data in cor_datas if not data == del_data]
    
    returned_eth_list = []
    for eth in args_eth_data:
        returned_eth_list.append(extract_ethernet(eth))

    assert returned_eth_list == cor_datas