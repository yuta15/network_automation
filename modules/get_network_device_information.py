from os import environ
import json

from .get_data import get_data
from .generate_all_interface_data import generate_all_interface_data


class Host:
    """
    ネットワーク機器のObject
    """
    def __init__(self, host, username, password) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.login = {'host': host, 'username': username, 'password': password}
        self.base_url = f'https://{self.host}/restconf/data'
        
        
    def get_hostdata(self):
        """
        説明追加
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
        説明追加
        """        
        urls = [self.base_url + '/openconfig-interfaces:interfaces']
        status_code_list, content_list = get_data(self.login, urls)
        interfaces_data = {}
        for interface_obj in content_list[0]['interface']:
            generate_all_interface_data(interface_obj)

        return interfaces_data