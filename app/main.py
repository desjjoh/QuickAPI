from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import router as items_router
from app.core.config import settings
from app.core.logging import setup_logging, log
from app.core.middleware import RequestLoggingMiddleware
from app.services.db import init_db, close_db

@asynccontextmanager
async def lifespan(_: FastAPI):
    setup_logging()
   
    log.info(
        "Server running in development mode at http://localhost:8000" if settings.debug else "Server running in production mode at http://localhost:8000",
        service=settings.app_name,
        port=8000,
    )

    log.info(
        "Swagger docs available at http://localhost:8000/docs",
        url="http://localhost:8000/docs",
        service=settings.app_name,
    )

    try:
        await init_db()
        log.info(
            "Startup complete",
            app=settings.app_name,
            mode="debug" if settings.debug else "production",
            db_connected=True,
        )
        yield
    except Exception as e:
        log.error("Startup failed", error=str(e))
        raise
    finally:
        try:
            await close_db()
            log.info("Shutdown complete", service=settings.app_name)
        except Exception as e:
            log.error("Error during shutdown", error=str(e))

app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)

app.include_router(items_router)
app.add_middleware(RequestLoggingMiddleware)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    log.warning(
        "HTTP exception raised",
        method=request.method,
        path=request.url.path,
        status=exc.status_code,
        detail=str(exc.detail or "No detail provided"),
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}