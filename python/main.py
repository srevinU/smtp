from fastapi import FastAPI, Body
from Smtp_server import Smtp
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    from_: str
    message: str

@app.post("/email/")
async def send_email(message: Message):
    myserver = Smtp()
    return myserver.send_email(from_=message.from_ ,message=message.message)