
from fastapi import FastAPI
import os
import socket

app = FastAPI(title="Time-based Scaling App")

@app.get("/")
def read_root():
    return {
        "message": "Hello from pod",
        "pod": os.getenv("HOSTNAME", socket.gethostname())
    }
