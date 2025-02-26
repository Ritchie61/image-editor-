from fastapi import FastAPI
import requests

app = FastAPI()

MICROSERVICES = {
    "file": "http://file-service:8001",
    "text": "http://text-service:8002",
    "image": "http://image-service:8003",
    "font": "http://font-service:8004",
}

@app.get("/")
async def root():
    return {"message": "API Gateway"}

@app.post("/upload")
async def upload(file):
    return requests.post(f"{MICROSERVICES['file']}/upload", files={"file": file}).json()

@app.post("/extract-text")
async def extract_text(file):
    return requests.post(f"{MICROSERVICES['text']}/extract", files={"file": file}).json()
