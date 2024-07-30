from fastapi import FastAPI, Body
from Smtp_server import Smtp
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import uvicorn
from pathlib import Path


app = FastAPI()
load_dotenv()

origins = os.environ['ORIGINS'].split(' ')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    from_: str
    message: str

@app.post("/smtp/email/")
async def send_email(message: Message):
    print(message)
    myserver = Smtp()
    return myserver.send_email(from_=message.from_ ,message=message.message)

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, reload=True)