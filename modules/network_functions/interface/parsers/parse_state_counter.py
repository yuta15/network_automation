

def parse_state_counter(int_counter_dict):
    """
    インターフェースのカウンタ情報を解析・成形するための関数
    args: 
        int_counter_dict:dict
    return: 
        return_int_counter_dict: dict
        {
            "in-unicast-pkts":
            "in-broadcast-pkts":
            "in-multicast-pkts":
            "in-errors":
            "in-fcs-errors":
            "out-unicast-pkts":
            "out-broadcast-pkts":
            "out-multicast-pkts":
            "out-errors":
            "out-fcs-errors":
            "last-clear":
        }
    """
    counter_keys = [
        'in-unicast-pkts',
        'in-broadcast-pkts',
        'in-multicast-pkts',
        'in-errors',
        'in-fcs-errors',
        'out-unicast-pkts',
        'out-broadcast-pkts',
        'out-multicast-pkts',
        'out-errors',
        'out-fcs-errors',
        'last-clear'
        ]
    return_int_counter_dict = {}
    for counter_key in counter_keys:
        return_int_counter_dict[counter_key] = int_counter_dict.get(counter_key)
    return return_int_counter_dict