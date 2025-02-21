from fastapi import APIRouter, UploadFile, File
from app.services import font_service

router = APIRouter(prefix="/fonts", tags=["Font Management"])

@router.post("/upload")
async def upload_font(file: UploadFile = File(...)):
    return await font_service.upload_font(file)

@router.get("/match")
async def match_font():
    return font_service.match_font()


