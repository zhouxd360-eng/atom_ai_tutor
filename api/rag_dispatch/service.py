class RAGDispatchService:
    def __init__(self):
        self.documents = []
    
    def search(self, query: str, student_id: int = None):
        results = []
        for doc in self.documents:
            if student_id is None or doc.get("student_id") == student_id:
                if query.lower() in doc.get("content", "").lower():
                    results.append(doc)
        return {"query": query, "student_id": student_id, "results": results}
    
    def upload_document(self, document: dict):
        doc_id = f"doc_{len(self.documents) + 1}"
        document["id"] = doc_id
        self.documents.append(document)
        return {"message": "Document uploaded", "document": document}
    
    def delete_document(self, doc_id: str):
        for i, doc in enumerate(self.documents):
            if doc.get("id") == doc_id:
                deleted = self.documents.pop(i)
                return {"message": "Document deleted", "document": deleted}
        return {"error": "Document not found", "doc_id": doc_id}