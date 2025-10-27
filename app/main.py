from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import router as items_router
from app.core.config import settings
from app.core.logging import setup_logging, log
from app.core.middleware import RequestLoggingMiddleware

@asynccontextmanager
async def lifespan(_: FastAPI):
    setup_logging()
    log.info("startup", app=settings.app_name, debug=settings.debug)
    yield
    log.info("shutdown", app=settings.app_name)

app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)
app.include_router(items_router)
app.add_middleware(RequestLoggingMiddleware)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    log.warning(
        "http_exception",
        path=request.url.path,
        status=exc.status_code,
        detail=str(exc.detail),
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}