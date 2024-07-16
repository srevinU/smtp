from fastapi import FastAPI, Body
from Smtp_server import Smtp
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()
origins = os.environ['ORIGINS'].split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    from_: str
    message: str

@app.post("/email/")
async def send_email(message: Message):
    print(message)
    myserver = Smtp()
    return myserver.send_email(from_=message.from_ ,message=message.message)