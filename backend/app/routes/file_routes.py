from fastapi import APIRouter, UploadFile, File
from app.services import file_service

router = APIRouter(prefix="/files", tags=["File Management"])

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await file_service.save_file(file)

@router.get("/download/{file_id}")
async def download_file(file_id: str):
    return file_service.get_file(file_id)

text_routes.py (Text Processing)
from fastapi import APIRouter, UploadFile, File
from app.services import text_service

router = APIRouter(prefix="/text", tags=["Text Processing"])

@router.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    return await text_service.extract_text(file)

@router.post("/edit")
async def edit_text(data: dict):
    return text_service.edit_text(data)


