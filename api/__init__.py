from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app(config):
    app = FastAPI(
        title=config["app"]["name"],
        version=config["app"]["version"],
        description=config["app"]["description"]
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.get("cors", {}).get("allow_origins", ["*"]),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    from api.student_info.routes import router as student_router
    from api.study_stat.routes import router as stat_router
    from api.rag_dispatch.routes import router as rag_router
    from api.plan_task.routes import router as plan_router
    from api.multimodal_upload.routes import router as upload_router
    
    app.include_router(student_router, prefix="/api/student", tags=["学生信息"])
    app.include_router(stat_router, prefix="/api/stat", tags=["学习统计"])
    app.include_router(rag_router, prefix="/api/rag", tags=["知识库检索"])
    app.include_router(plan_router, prefix="/api/plan", tags=["学习计划"])
    app.include_router(upload_router, prefix="/api/upload", tags=["文件上传"])
    
    @app.get("/")
    async def root():
        return {"message": "atom_ai_tutor API Server"}
    
    return app