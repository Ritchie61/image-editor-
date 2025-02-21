import shutil
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

async def save_file(file):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "path": str(file_path)}

def get_file(file_id):
    file_path = UPLOAD_DIR / file_id
    if file_path.exists():
        return {"path": str(file_path)}
    return {"error": "File not found"}


