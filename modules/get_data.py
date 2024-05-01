import requests
from requests.auth import HTTPBasicAuth
import json


def get_interface_data(user, password, header, url):
    request_return = requests.get(url, auth=HTTPBasicAuth(user, password), headers=header, verify=False)
    return_json = json.loads(request_return.content)
    return return_json