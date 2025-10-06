
# app-a/app.py
from fastapi import FastAPI
import os
import socket

app = FastAPI(title="App A")

@app.get("/")
def read_root():
    return {
        "app": "A",
        "message": "Hello from App A",
        "pod": os.getenv("HOSTNAME", socket.gethostname())
    }
