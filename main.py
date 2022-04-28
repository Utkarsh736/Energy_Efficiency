from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/')
def home():
    return{'Energy':'Efficiency'}