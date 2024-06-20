import os
import json
import pytest
import jmespath


@pytest.fixture(autouse=True)
def conf():
    """
    pytest事前、事後処理設定
    """
    def _conf(type, json_paths):
        """
        初期化関数
        args:
            type:str
                取得するデータタイプを指定する。interface, nw-instance等
            json_paths:list
                取得したいパスを指定する。jmespath形式
                '.'を指定した場合、Jsonデータをloadsしてreturn
                それ以外は指定したパスの情報を取得してreturn
        returns:
            data:list
                指定したパスをリスト化したもの
        """
        data = []
        match type:
            case 'interface':
                path = os.getcwd() + '/example_interface.json'
            case 'nw_instance':
                path = os.getcwd() + '/example_nw_instance.json'
            
        with open(path, mode='r') as f:
            base_data = json.loads(f.read())
        for json_path in json_paths:
            if not json_path == '.':
                data.append(jmespath.search(json_path, base_data))
            else:
                data.append(base_data)
        return data

    return _conf

