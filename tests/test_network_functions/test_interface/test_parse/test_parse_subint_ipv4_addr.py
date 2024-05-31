import itertools
import json

from noa.network_functions.interface.parsers.parse_subint_ipv4_addr import parse_subint_ipv4_addr
from tests.test_network_functions.test_interface.test_parse.parse_data import test_parse_subint_ipv4_addr


def test_parse_subint_ipv4_addr():
    '''
    parse_subint_ipv4_addrをテストする関数
    
    
    '''
    
    path = '/tmp/network_automation/example_interface.json'
    with open(path, mode='r') as f:
        data = json.loads(f.read())
    print(data)
        
        
test_parse_subint_ipv4_addr()