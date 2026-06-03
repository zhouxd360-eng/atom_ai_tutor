from fastapi import APIRouter, Query
from api.rag_dispatch.service import RAGDispatchService

router = APIRouter()
service = RAGDispatchService()

@router.get("/search")
async def search_knowledge(query: str = Query(...), student_id: int = None):
    return service.search(query, student_id)

@router.post("/upload")
async def upload_document(document: dict):
    return service.upload_document(document)

@router.delete("/document/{doc_id}")
async def delete_document(doc_id: str):
    return service.delete_document(doc_id)