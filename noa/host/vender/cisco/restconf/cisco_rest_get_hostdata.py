


from noa.control.get_data_rest import get_data_rest


def cisco_rest_get_hostdata(login_params):
    """
    cisco用ホストデータ取得用関数
    args:
        target: str
            情報を取得するネットワーク機器のドメイン or IP address
        username: str
            ユーザ名の文字列
        password: str
            パスワードの文字列
        port: int
            NW機器へアクセスするための宛先ポート番号
        model: str
            使用するYang-model. 取得できるデータが異なる。
    return: dict
        {
            hostname: str,
            OS: str,
            s/n: str
            license: str
        }
    """
    if login_params['model'] == 'openconfig':
        urls = [
            f'https://{login_params['taraget']}:{login_params['port']}restconf/data/Cisco-IOS-XE-native:native/version', 
            f'https://{login_params['taraget']}:{login_params['port']}restconf/data/Cisco-IOS-XE-native:native/license/udi/sn'            
        ]
    elif login_params['model'] == 'cisco':
        urls = [
            f'https://{login_params['taraget']}:{login_params['port']}restconf/data/Cisco-IOS-XE-native:native/version', 
            f'https://{login_params['taraget']}:{login_params['port']}restconf/data/Cisco-IOS-XE-native:native/license/udi/sn'
            ]
        
    host_data = get_data_rest(
        {'host': login_params['target'], 'username': login_params['username'], 'password': login_params['password']}, 
        urls
        )
    
    