from fastapi import FastAPI
from app.api.routes import router as items_router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.version)
app.include_router(items_router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}