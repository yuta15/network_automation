import requests
from requests.auth import HTTPBasicAuth
import json


def get_data(login_data:object, urls:list):
    status_code = []
    content_data = []
    get_headers = {'Accept': 'application/yang-data+json'}
    session = requests.Session()
    # try/exceptでエラー処理を記述。タイムアウト時に処理停止する。
    for url in urls:
        data = session.get(url, auth=HTTPBasicAuth(login_data["username"], login_data["password"]), headers=get_headers, verify=False)
        status_code.append(data.status_code)
        content_data_origin = binaryToDict(data.content)
        for content in content_data_origin.values():
            content_data.append(content)
    session.close()
    return status_code,content_data


# binary -> Dict変換用関数
def binaryToDict(content):
    return_data = json.loads(content.decode())
    return return_data
