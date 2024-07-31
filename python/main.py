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
    instance: str

class EmailResponse(BaseModel):
    status: int
    message: str

@app.post("/smtp/email/")
async def send_email(message: Message):
    print(message)
    myserver = Smtp()
    result = myserver.send_email(from_=message.from_ ,message=message.message, instance=message.instance)
    return EmailResponse(status=result['status'], message=result['message'])

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", host="smtp_server", port=5430, reload=True)