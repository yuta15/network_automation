from noa.control.get_data_rest import get_data_rest
from noa.data_format.openconfig.restconf.interface.interface import interface
from noa.data_format.vender.cisco.interface.cisco_int import cisco_int

def cisco_rest_get_interface(login_params):
    """
    Cisco機器へのRESTCONFを使用したインターフェース情報を取得する関数
    args:
        login_params:
    """
    base_url = f'https://{login_params.target}/restconf/data'
    
    if login_params['model'] is 'openconfig':
        urls = [f'{base_url}/openconfig-interfaces:interfaces']
        int_data = get_data_rest(login_data=login_params, urls=urls)
        int_data = interface(int_data)
        return int_data
    
    elif login_params['model'] is 'cisco':
        urls = [f'{base_url}/Cisco-IOS-XE-native:native/interface']
        int_data = get_data_rest(login_data=login_params, urls=urls)
        int_data = cisco_int(int_data)
        return int_data