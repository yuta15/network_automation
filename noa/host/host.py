

from noa.control.get_data_rest import get_data_rest
from noa.host.vender.cisco.restconf.cisco_rest_get_hostdata import cisco_rest_get_hostdata
from noa.host.vender.cisco.restconf.cisco_rest_get_interface import cisco_rest_get_interface
from noa.host.vender.cisco.restconf.cisco_rest_get_interfaces import cisco_rest_get_interfaces

from noa.network_functions.interface.interface import interface
from noa.network_functions.interface.interfaces import interfaces


class Host:
    """
    ネットワーク機器のClass
    remarks:
        get以外の機能は未実装
    """
    def __init__(self, target:str, username:str, password:str, vender:str, port:int=None, method:str=None, model:str=None) -> None:
        """
        args:
            target: str
                情報を取得するネットワーク機器のドメイン or IP address
            username: str
                ユーザ名の文字列
            password: str
                パスワードの文字列
            vender: str
                NW機器のベンダー名
            port: int
                NW機器へアクセスするための宛先ポート番号
            method: str
                NW機器へアクセスするためのインターフェース. restconf,netconf,gnmi,gnoi等
            model: str
                使用するYang-model. 取得できるデータが異なる。
            return: None
        """
        self.method = method if not method is None else 'gnmi'
        self.vender = vender
        self.model = model if not model is None else self.vender 
        self.match_case = [vender, method]
        self.login_params = {'target': target, 'username': username, 'password': password, 'port':port, 'model': model}


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
            venderの値毎に関数を分割。
        """
        match self.match_case:
            case ['cisco', 'restconf']:
                host_data = cisco_rest_get_hostdata(self.login_params)
                return host_data
            # case ['cisco', 'netconf']:
            #     host_data = cisco_net_get_hostdata(login_params)
            #     return host_data
            # case ['cisco', 'gnmi']:
            #     host_data = cisco_gnmi_get_hostdata(login_params)
            #     return host_data
            # case ['paloalto', 'rest']:
            #     host_data = palo_rest_get_hostdata(login_params)
            #     return host_data
            
    
    
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
        match self.match_case:
            case ['cisco', 'restconf']:
                
                urls = [self.base_url + '/openconfig-interfaces:interfaces']
        status_code_list, content_list = get_data_rest(self.login, urls)
        return_interfaces_data = None
        for content in content_list:
            return_interfaces_data = interfaces(content.get('interface'))
        return return_interfaces_data