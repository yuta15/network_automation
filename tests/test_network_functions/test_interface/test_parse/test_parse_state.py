import itertools

from noa.network_functions.interface.parsers.parse_state import parse_state
from tests.test_network_functions.test_interface.test_parse.parse_data import test_parse_state_data

def test_parse_state():
    '''
    parse_state関数をテストするための関数
    仮のデータを渡して想定通りの結果が得られるか確認する。
    {
        enabled:
        admin-status:
        oper-status:
        last-change:
    }
    '''
    enabled_key = 'enabled'
    admin_status_key = 'admin-status'
    oper_status_key = 'oper-status'
    last_change_key = 'last-change'
    
    enabled_vals = [True, False, None]
    admin_status_vals = ['UP', 'DOWN', None]
    oper_status_vals = ['UP', 'DOWN', None]
    last_change_vals = ['1715487320107000000', None]
    
    state_vals_combs = itertools.product(enabled_vals, admin_status_vals, oper_status_vals, last_change_vals)
    
    for state_vals_comb in state_vals_combs:
        test_parse_state_data[enabled_key] = state_vals_comb[0]
        test_parse_state_data[admin_status_key] = state_vals_comb[1]
        test_parse_state_data[oper_status_key] = state_vals_comb[2]
        test_parse_state_data[last_change_key] = state_vals_comb[3]
        current_data = {
            enabled_key: state_vals_comb[0], 
            admin_status_key: state_vals_comb[1], 
            oper_status_key: state_vals_comb[2], 
            last_change_key: state_vals_comb[3]
        }
        
        parse_state_data = parse_state(test_parse_state_data)
        assert parse_state_data == current_data