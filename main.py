from fastapi import FastAPI

from modules import interface

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/interfaces')
async def get_interfaces():
    data = interface.get_interface_all()
    return data