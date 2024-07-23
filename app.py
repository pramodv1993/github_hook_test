from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/postreceive/")
async def display_msg(data: Dict):
    received_data = {"message_received": data}
    print(received_data)
    return received_data

