import os
import socket
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

INSTANCE_ID = os.getenv("INSTANCE_ID", "unknown")
CONTAINER_ID = socket.gethostname()


@app.get("/")
async def index(request: Request):
    return {
        "instance_id": INSTANCE_ID,
        "container_id": CONTAINER_ID,
        "message": f"Handled by {INSTANCE_ID} (container: {CONTAINER_ID[:12]})",
        "proxy_headers": {
            "x-real-ip": request.headers.get("x-real-ip"),
            "x-forwarded-for": request.headers.get("x-forwarded-for"),
            "x-forwarded-proto": request.headers.get("x-forwarded-proto"),
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok", "instance": INSTANCE_ID}
