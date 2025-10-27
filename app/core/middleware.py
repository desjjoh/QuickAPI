import time
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging import log

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        try:
            response: Response = await call_next(request)
        except Exception as exc:
            log.exception("unhandled_exception", path=request.url.path, error=str(exc))
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"},
            )

        process_time = (time.perf_counter() - start_time) * 1000
        log.info(
            "request_handled",
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration_ms=round(process_time, 2),
        )
        return response