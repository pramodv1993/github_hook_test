from fastapi import FastAPI, Request
from typing import Dict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/postreceive/")
async def display_msg(req: Request):
    received_data = await req.body()
    received_data = received_data.decode('utf-8')
    print(received_data)
    # if req.headers['Content-Type'] == 'application/json':
    #     item = await req.json()
    # elif req.headers['Content-Type'] == 'multipart/form-data':
    #     item = await req.form()
    # elif req.headers['Content-Type'] == 'application/x-www-form-urlencoded':
    #     item = await req.form()
    # received_data = {"message_received": item}
    return received_data

