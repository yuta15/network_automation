import requests
from requests.auth import HTTPBasicAuth
import json


def get_data(login_data, urls):
    """
    用途：
        ネットワーク機器から情報を取得する為の関数。
    
    引数：
        login_data: dict
            ホスト情報を以下のフォーマットで登録
            {"host": host, "username": username, "password": password}
            
        urls: list
            取得する情報のURL一覧
            
    Return: dict
    """
    
    status_code = []
    content_data = []
    get_headers = {'Accept': 'application/yang-data+json'}
    session = requests.Session()
    # try/exceptでエラー処理を記述。タイムアウト時に処理停止する。
    for url in urls:
        data = session.get(url, auth=HTTPBasicAuth(login_data["username"], login_data["password"]), headers=get_headers, verify=False)
        status_code.append(data.status_code)
        content_data_origin = json.loads(data.content)
        for content in content_data_origin.values():
            content_data.append(content)
    session.close()
    return status_code,content_data