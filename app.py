from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/postreceive")
async def display_msg(data):
    return {"message_received": data}

