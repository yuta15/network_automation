import jmespath

def generate_test_data_eth(eth_data):
    """
    jsonデータからテスト用の正解データを生成する。
    args:
        eth_data: list
          - openconfig-if-ethernet:ethernet配下のdictのリスト
    returned: 
        correct_datas: list
          - 正解データのリスト
    """
    mac_add_path = '"openconfig-if-ethernet:ethernet".state."mac-address"'
    auto_nego_path = '"openconfig-if-ethernet:ethernet".state."auto-negotiate"'
    port_speed_path = '"openconfig-if-ethernet:ethernet".state."port-speed"'
    duplex_path = '"openconfig-if-ethernet:ethernet".state."negotiated-duplex-mode"'
    
    data_path = f'[*].{{"mac-address": {mac_add_path}, "auto-negotiate": {auto_nego_path},"port-speed": {port_speed_path},"negotiated-duplex-mode": {duplex_path}}}[]'
    correct_datas = jmespath.search(data_path, eth_data)
    
    return correct_datas