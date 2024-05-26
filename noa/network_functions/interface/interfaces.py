


from noa.network_functions.interface.interface import interface


def interfaces(all_interface_list):
    """
    複数のインターフェースの情報をマージする関数
    args:
        all_interface_dict: dict
            すべてのインターフェース情報
    return: dict
        {
            interfase_name1:{}
            interfase_name2:{}
            interfase_name3:{}
        }
    remarks:
    """
    return_all_interfaces = {}
    for interface_dict in all_interface_list:
        return_all_interfaces = return_all_interfaces | interface(interface_dict)
    return return_all_interfaces