import os
import itertools

from noa.network_functions.interface.parsers.parse_ethernet import parse_ethernet
from tests.test_network_functions.test_interface.test_parse.parse_data import test_ethernet_data



def test_parse_ethernet():
    '''
    parse_ethernetをテストするための関数。
    チェックしたい値のすべての組み合わせで動作するか確認する。
    '''
    # チェックしたいキーを指定
    mac_addr_key = 'mac-address'
    auto_negotiate_key = 'auto-negotiate'
    port_speed_key = 'port-speed'
    duplex_key = 'negotiated-duplex-mode'

    # テストデータへ代入する値は以下
    mac_addr_list = ["52:54:00:10:73:00", None]
    auto_negotiate_list = [True, None]
    duplex_list = ['FULL',  None]
    port_speed_list = ['openconfig-if-ethernet:SPEED_1GB', None]

    eth_data_combs = itertools.product(mac_addr_list, auto_negotiate_list, duplex_list, port_speed_list)

    for eth_data_comb in eth_data_combs:
        test_ethernet_data[mac_addr_key] = eth_data_comb[0]
        test_ethernet_data[auto_negotiate_key] = eth_data_comb[1]
        test_ethernet_data[port_speed_key] = eth_data_comb[2]
        test_ethernet_data[duplex_key] = eth_data_comb[3]
        parse_eth_data = parse_ethernet(test_ethernet_data)
        
        assert parse_eth_data[mac_addr_key] == eth_data_comb[0]
        assert parse_eth_data[auto_negotiate_key] == eth_data_comb[1]
        assert parse_eth_data[port_speed_key] == eth_data_comb[2]
        assert parse_eth_data[duplex_key] == eth_data_comb[3]
    
