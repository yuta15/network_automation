import os
import json
import pytest
import jmespath


@pytest.fixture(autouse=True)
def conf():
    """
    pytest事前、事後処理設定
    """
    def _conf(json_paths):
        path = os.getcwd() + '/example_interface.json'
        data = []
        with open(path, mode='r') as f:
            base_data = json.loads(f.read())
        for json_path in json_paths:
            data.append(jmespath.search(json_path, base_data))
        return data

    return _conf

