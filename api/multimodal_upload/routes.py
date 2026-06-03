from fastapi import APIRouter, File, UploadFile
from api.multimodal_upload.service import MultimodalService

router = APIRouter()
service = MultimodalService()

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    return await service.upload_image(file)

@router.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    return await service.upload_audio(file)

@router.post("/video")
async def upload_video(file: UploadFile = File(...)):
    return await service.upload_video(file)

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    return await service.upload_pdf(file)