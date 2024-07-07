

def test_fdb(conf):
    """
    nw-instanceのfdbをテストするための関数。
    example_network-instance.jsonから抽出し、返り値が想定通りであることを確認する。
    {
        name: str,
        type: str,
        description: str,
        router-id: str,
        route-distinguisher: str,
    }
    """
    