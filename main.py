from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class RequestMessage(BaseModel):
    text: str

@app.get('/')
def index():
  return HTMLResponse('<h1>A self-documenting web app v1</h1>')

@app.post('/generate')
def generate(request: RequestMessage):
  result = {
    "errcode": 0,
    "errmsg": "",
    "echo": request
  }
  return result  
