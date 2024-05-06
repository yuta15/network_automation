import copy
import json
from ncclient import manager

from Application.modules import get_data


def get_version():
    USER = "cisco"
    PASS = "cisco"
    host = "172.18.1.2"
    base_api_url = f"https://{host}/restconf/data/Cisco-IOS-XE-native:native"
    data = get_data.get_data(USER, PASS, base_api_url)
    data = json.loads(data.content)
    return data
    
