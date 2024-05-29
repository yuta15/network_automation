import os
import json

from noa.network_functions.interface.parsers.parse_ethernet import parse_ethernet

def test_parse_ethernet():
    path = f'{os.getcwd()}/tests/test_network_functions/test_interface/test_parse/parse_ethernet.json'
    key_str = 'openconfig-if-ethernet:ethernet'
    
    with open(path, mode='r') as f:
        ethernet_dict = json.loads(f.read())
    ethernet_data = parse_ethernet(ethernet_dict.get(key_str))
    
    assert ethernet_data['mac-address'] == '52:54:00:10:73:00'
    assert ethernet_data['auto-negotiate'] == True
    assert ethernet_data['port-speed'] == 'openconfig-if-ethernet:SPEED_1GB'
    assert ethernet_data['negotiated-duplex-mode'] == 'FULL'
