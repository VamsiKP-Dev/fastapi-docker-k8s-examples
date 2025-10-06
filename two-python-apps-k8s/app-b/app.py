
# app-b/app.py
from fastapi import FastAPI
import os
import socket

app = FastAPI(title="App B")

@app.get("/")
def read_root():
    return {
        "app": "B",
        "message": "Hello from App B",
        "pod": os.getenv("HOSTNAME", socket.gethostname())
    }
