import jmespath


def genr_subif(subint_data):
    """
    subintのテスト用データを生成する関数
    args:
        subint_data: list
          - subinterface配下のリスト
    returned:
        subints_data: list
          - subintのテスト用データ
    """
    enabled_path = 'state.enabled'
    admin_status_path = 'state."admin-status"'
    oper_status_path = 'state."oper-status"'
    last_change_path = 'state."last-change"'
    ip_path = '"openconfig-if-ip:ipv4".addresses.address[].state.ip'
    prefix_length_path = '"openconfig-if-ip:ipv4".addresses.address[].state."prefix-length"'
    description_path = 'config.description'
    
    data_paths = f'[].{{enabled: {enabled_path},"admin-status": {admin_status_path}, "oper-status": {oper_status_path}, "last-change": {last_change_path}, ip: {ip_path}, "prefix-length": {prefix_length_path}, description: {description_path}}}[]'
    index_path = '[].index[]'
    correct_subint_data = jmespath.search(data_paths, subint_data)
    correct_index_data = jmespath.search(index_path, subint_data)

    correct_subints = {}
    for index, subint_data in zip(correct_index_data, correct_subint_data):
        correct_subints[index] = subint_data
    return correct_subints