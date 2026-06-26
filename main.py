from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




class EchoItem(BaseModel):
    text: str

    
@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/echo")
async def echoBack(item: EchoItem):
    return item.text




