from fastapi import APIRouter, UploadFile, File
from app/services import text_service

router = APIRouter(prefix="/text", tags=["Text Processing"])

@router.post("/extract")
async def extract_text(file: UploadFile = File(None)):
    return await text_service.extract_text(file)

@router.post("/edit")
async def edit_text(data: dict):
    return text_service.edit_text(data)
