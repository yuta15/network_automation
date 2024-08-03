import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

from noa.host.host import Host
from noa.host.vender.cisco.cisco import Cisco

app = FastAPI()


class Device(BaseModel):
    address: str
    dst_port: int
    vender: Union[str, None] = None
    method: Union[str, None] = None


class Auth(BaseModel):
    username: str
    password: str
    cert: Union[str, None] = None

# --------------------------------------
# FastAPI tutorial
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
# --------------------------------------

HOST = os.environ.get('NETWORK_TEST_HOST')
USERNAME = os.environ.get('NETWORK_TEST_USERNAME')
PASSWORD = os.environ.get('NETWORK_TEST_PASSWORD')


@app.post('/host')
async def get_hostdata(device: Device, auth: Auth):
    match device.vender:
        case "cisco":
            host = Cisco(target=device.address, username=auth.username, password=auth.password)
        # case "fortinet":
            
    # host = Host(device.address, auth.username, auth.password)
    data = host.get_hostdata()
    return data


@app.post('/interfaces')
async def get_interfaces(device: Device, auth: Auth):
    host = Host(device.address, auth.username, auth.password)
    all_interfaces_data = host.get_interface_all()
    return all_interfaces_data


@app.get('/interfaces/{interface_name}')
async def get_interface(interface_name: str, device: Device, auth: Auth):
    host = Host(device.address, auth.username, auth.password, interface_name)
    data = host.get_interface_info()
    return data