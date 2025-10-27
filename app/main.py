from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router as items_router
from app.core.config import settings
from app.core.logging import setup_logging, log

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    log.info("startup", app=settings.app_name, debug=settings.debug)
    yield
    log.info("shutdown", app=settings.app_name)

app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)
app.include_router(items_router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}