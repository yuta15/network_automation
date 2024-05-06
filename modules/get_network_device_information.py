from os import environ
import json

from .get_data import get_data


class Host:
    def __init__(self, host, username, password) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.login = {"host": host, "username": username, "password": password}
        self.base_url = f'https://{self.host}/restconf/data'
        
        
    # host情報を取得する。
    def get_hostdata2(self):
        urls = [
            self.base_url + '/Cisco-IOS-XE-native:native/version',
            self.base_url + '/Cisco-IOS-XE-native:native/license/udi/sn',
        ]
        dict_keys = ["version", "s/n"]
        staus_code_list, content_list = get_data(self.login, urls)
        # status_codeを使用した条件分岐
        data = {key : value for key, value in zip(dict_keys, content_list)}
        return data