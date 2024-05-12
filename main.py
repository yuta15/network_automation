import json
import os
from fastapi import FastAPI

from modules.get_network_device_information import Host

app = FastAPI()

# --------------------------------------
# FastAPI tutorial
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
# --------------------------------------

HOST = os.environ.get('NETWORK_TEST_HOST')
USERNAME = os.environ.get('NETWORK_TEST_USERNAME')
PASSWORD = os.environ.get('NETWORK_TEST_PASSWORD')


# すべての機器のhost情報をとってくる。
# @app.get('/hosts')
# async def get_host_list():


# @app.get('/status/{host}/hostdata')
# 検証用として以下を使用。本当は上記のパスにしたい。
# 特定の機器のhost情報を取得
# @app.get('/status/{host}')
# 上記を使用予定。検証の為以下を使用。
@app.get('/host')
async def get_hostdata():
    host = Host(HOST, USERNAME, PASSWORD)
    data = host.get_hostdata()
    data = json.dumps(data)
    return data


@app.get('/interfaces')
async def get_interfaces():
    host = Host(HOST, USERNAME, PASSWORD)
    all_interfaces_data = json.dumps(host.get_interface_all())
    return all_interfaces_data


@app.get('/interfaces/{interface_name}')
async def get_interfaces(interface_name: str):
    host = Host(HOST, USERNAME, PASSWORD, interface_name)
    data = host.get_interface_info()
    return data


@app.get('/interfaces/{interface_name}/FHRP')
async def get_interface_fhrp(interface_name: str):
    host = Host(HOST, USERNAME, PASSWORD, interface_name)
    data = host.get_interface_info()
    return data