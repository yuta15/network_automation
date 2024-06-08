import jmespath
from jmespath.exceptions import JMESPathError, JMESPathTypeError

def extract_ethernet(eth_dict: dict) -> dict:
    """
    引数で受け取ったデータから情報を抽出するための関数
    
    :arg eth_dict: dict
        openconfig-if-ethernet:ethernet内のdict
    
    :returns return_eth_dict: dict
        openconfig-if-ethernet:ethernet内のdictから必要な情報を抽出したもの
        {
            "mac-address": str,
            "auto-negotiate": str,
            "port-speed": str,
            "negotiated-duplex-mode": str 
        }
    """
    mac_addr = 'mac-address'
    auto_nego = 'auto-negotiate'
    port_speed = 'port-speed'
    duplex = 'negotiated-duplex-mode'
    keys = [mac_addr, auto_nego, port_speed, duplex]
    dict_path = f'state.["{mac_addr}", "{auto_nego}", "{port_speed}", "{duplex}"]'
    
    eth_datas = jmespath.search(dict_path, eth_dict)
    # print(eth_datas)
    print(jmespath.search(dict_path, eth_dict))
    return_eth_dict = dict(zip(keys, eth_datas))
    
    return return_eth_dict 
    
    