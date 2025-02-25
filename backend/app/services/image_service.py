import cv2
import numpy as np

async def segment_image(file):
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    return {"message": "Image segmented", "edges": edges.tolist()}

def replace_image(data):
    return {"message": "Image replaced successfully"}
