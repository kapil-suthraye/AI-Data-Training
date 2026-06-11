import logging
import time

from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware

from prometheus_client import Counter


REQUEST_COUNT = Counter(
    "request_count_total",
    "Total API Requests",
    ["method", "path"]
)


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = str(uuid4())

        start = time.perf_counter()

        response = await call_next(request)

        duration_ms = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        REQUEST_COUNT.labels(
            method=request.method,
            path=request.url.path
        ).inc()

        logging.info(
            f"request_id={request_id} "
            f"method={request.method} "
            f"path={request.url.path} "
            f"status_code={response.status_code} "
            f"duration_ms={duration_ms}"
        )

        response.headers["X-Request-ID"] = request_id

        return response