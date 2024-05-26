

from noa.network_functions.interface.merge.merge_subint import merge_subint


def merge_all_subint(sub_int_list) -> dict:
    """
    単一のサブインターフェースの情報をマージするための関数。
    args:
        interface_subint: dict
    return: dict
        以下の形式で応答
        {
            subint_index1:{},
            subint_index1:{},
            subint_index1:{},
        }
    remarks:
        現状、すべてのサブインターフェース情報が取れていない。
        一度実行後、デバッグをする。
    """
    return_sub_ints_dict = {}
    sub_int_data_dict = {}
    sub_int_dict = {}
    for sub_int in sub_int_list:
        sub_int_dict = merge_subint(sub_int)
        sub_int_data_dict = sub_int_data_dict | sub_int_dict
    return_sub_ints_dict['subinterfaces'] = sub_int_dict
    return return_sub_ints_dict