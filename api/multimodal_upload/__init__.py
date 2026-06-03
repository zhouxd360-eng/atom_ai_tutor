from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    return {"message": "Image uploaded", "filename": file.filename}

@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    return {"message": "Audio uploaded", "filename": file.filename}

@router.post("/video")
async def upload_video(file: UploadFile = File(...)):
    return {"message": "Video uploaded", "filename": file.filename}

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    return {"message": "PDF uploaded", "filename": file.filename}