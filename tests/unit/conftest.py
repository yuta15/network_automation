import os
import json
import pytest
import jmespath


@pytest.fixture(autouse=True)
def conf():
    """
    pytest事前、事後処理設定
    """
    def _conf(json_path):
        path = os.getcwd() + '/example_interface.json'
        with open(path, mode='r') as f:
            base_data = json.loads(f.read())
        data = jmespath.search(json_path, base_data)
        return data
    
    return _conf

