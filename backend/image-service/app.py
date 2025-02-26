from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import io

app = FastAPI()

@app.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    image = np.array(bytearray(await file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    _, encoded_img = cv2.imencode(".png", edges)
    return {"image": encoded_img.tobytes()}
