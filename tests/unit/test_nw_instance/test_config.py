from noa.network_functions.nw_instance import config


def test_config(conf):
    """
    nw-instanceのconfigをテストするための関数。
    example_network-instance.jsonから抽出し、返り値が想定通りであることを確認する。
    {
        name: str,
        type: str,
        description: str,
        router-id: str,
        route-distinguisher: str,
    }
    """
    