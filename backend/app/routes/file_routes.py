from fastapi import APIRouter, UploadFile, File
from app.services import file_service

router = APIRouter(prefix="/files", tags=["File Management"])

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await file_service.save_file(file)

@router.get("/download/{file_id}")
async def download_file(file_id: str):
    return file_service.get_file(file_id)
