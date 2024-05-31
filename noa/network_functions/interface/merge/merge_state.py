

from noa.network_functions.interface.parsers.parse_state import parse_state
from noa.network_functions.interface.parsers.parse_state_counter import parse_state_counter


def merge_state(int_state_dict, counter: bool = False):
    """
    parse関数にて抽出・成形したデータをマージするための関数
    args:
        int_state_dir: dict
    retrun: 
        return_int_state_dict: dict
        
    remarks:
        parse_state_counter関数を呼び出す処理追加予定。
    """
    return_int_state_dict = {}
    if counter:
        return_int_state_dict['counter'] = parse_state_counter(int_state_dict.get('counter'))
    return_int_state_dict = return_int_state_dict | parse_state(int_state_dict)
    return return_int_state_dict