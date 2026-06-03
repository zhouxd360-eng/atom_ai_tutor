from fastapi import UploadFile
from pathlib import Path
from datetime import datetime
import aiofiles

class MultimodalService:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent.parent / "data" / "raw_resources"
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    async def _save_file(self, file: UploadFile, sub_dir: str) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = Path(file.filename).suffix
        filename = f"{timestamp}{ext}"
        
        file_dir = self.base_dir / sub_dir
        file_dir.mkdir(parents=True, exist_ok=True)
        file_path = file_dir / filename
        
        contents = await file.read()
        async with aiofiles.open(file_path, "wb") as f:
            await f.write(contents)
        
        return str(file_path)
    
    async def upload_image(self, file: UploadFile):
        file_path = await self._save_file(file, "images")
        return {"message": "Image uploaded", "filename": file.filename, "path": file_path}
    
    async def upload_audio(self, file: UploadFile):
        file_path = await self._save_file(file, "record_audio")
        return {"message": "Audio uploaded", "filename": file.filename, "path": file_path}
    
    async def upload_video(self, file: UploadFile):
        file_path = await self._save_file(file, "videos")
        return {"message": "Video uploaded", "filename": file.filename, "path": file_path}
    
    async def upload_pdf(self, file: UploadFile):
        file_path = await self._save_file(file, "pdfs")
        return {"message": "PDF uploaded", "filename": file.filename, "path": file_path}