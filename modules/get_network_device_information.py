from os import environ
import json

from .get_data import get_data
from .merge_interface import merge_interfaces


class Host:
    """
    ネットワーク機器のClass
    args:
        host: str
            情報を取得するネットワーク機器のドメイン or IP address
        username: str
            ユーザ名の文字列
        password: str
            パスワードの文字列
    return: None
    remarks:
        get以外の機能は未実装
    """
    def __init__(self, host, username, password) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.login = {'host': host, 'username': username, 'password': password}
        self.base_url = f'https://{self.host}/restconf/data'
        
        
    def get_hostdata(self):
        """
        OSバージョン、S/N、稼働時間を取得する関数。
        現状、OSバージョン、S/Nのみ取得可能。
        args:

        return:
            host_data: dict
            {
                'version': str, 
                's/n':str, 
                *up_time, str
            }
            *未実装
        remarks:
            Cisco固有のpathを使用しているため、OpenConfigにて実装可能である場合は修正
        """
        urls = [
            self.base_url + '/Cisco-IOS-XE-native:native/version',
            self.base_url + '/Cisco-IOS-XE-native:native/license/udi/sn',
        ]
        dict_keys = ['version', 's/n']
        staus_code_list, content_list = get_data(self.login, urls)
        # status_codeを使用した条件分岐
        host_data = {key : value for key, value in zip(dict_keys, content_list)}
        return host_data
    
    
    def get_interface_all(self):
        """
        全インターフェース情報を取得する関数
        args: 
        
        return:
            return_interfaces_data: dict
            インターフェース情報をDictでreturn
        remarks:
            OpenConfigで実装。
            Cisco機器からはVLAN情報は取得できないためVLAN情報については未実装
            Cisco独自のpathから取得可能であることは確認済みの為、条件分岐で実装。
        """        
        urls = [self.base_url + '/openconfig-interfaces:interfaces']
        status_code_list, content_list = get_data(self.login, urls)
        return_interfaces_data = None
        for content in content_list:
            return_interfaces_data = merge_interfaces(content.get('interface'))
        return return_interfaces_data