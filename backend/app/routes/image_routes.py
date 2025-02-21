from fastapi import APIRouter, UploadFile, File
from app.services import image_service

router = APIRouter(prefix="/image", tags=["Image Processing"])

@router.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    return await image_service.segment_image(file)

@router.post("/replace")
async def replace_image(data: dict):
    return image_service.replace_image(data)

