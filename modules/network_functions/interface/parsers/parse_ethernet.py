


def parse_ethernet(ethernet_state_dict):
    """
    ethernetデータのstate情報を抽出・成形するための関数
    args:
        ethernet_state_dict: dict
    return:
        return_ethernet_state_dict: dict
        {
            "mac-address":
            "auto-negotiate":
            "port-speed":
            "negotiated-duplex-mode"
        }
    remarks:
    """
    ethernet_state_keys = ["mac-address", "auto-negotiate", "port-speed", "negotiated-duplex-mode"]
    return_etheret_dict = {}
    for ethernet_key in ethernet_state_keys:
        return_etheret_dict[ethernet_key] = ethernet_state_dict.get(ethernet_key)
    return return_etheret_dict
