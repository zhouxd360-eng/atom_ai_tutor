from fastapi import APIRouter, File, UploadFile
from pathlib import Path
from datetime import datetime
import aiofiles

router = APIRouter()

UPLOAD_DIR = Path(__file__).parent.parent.parent / "data" / "raw_file"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def save_file(file: UploadFile, sub_dir: str = "") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = Path(file.filename).suffix
    filename = f"{timestamp}{ext}"
    
    if sub_dir:
        file_dir = UPLOAD_DIR / sub_dir
        file_dir.mkdir(parents=True, exist_ok=True)
        file_path = file_dir / filename
    else:
        file_path = UPLOAD_DIR / filename
    
    contents = await file.read()
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(contents)
    
    return str(file_path)

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    file_path = await save_file(file, "images")
    return {"message": "Image uploaded", "filename": file.filename, "path": file_path}

@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    file_path = await save_file(file, "audio")
    return {"message": "Audio uploaded", "filename": file.filename, "path": file_path}

@router.post("/video")
async def upload_video(file: UploadFile = File(...)):
    file_path = await save_file(file, "video")
    return {"message": "Video uploaded", "filename": file.filename, "path": file_path}

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = await save_file(file, "pdf")
    return {"message": "PDF uploaded", "filename": file.filename, "path": file_path}