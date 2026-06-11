from fastapi import FastAPI

from config import load_config
from schemas import SummariseRequest
from schemas import SummariseResponse
from llm_client import generate_summary

from middleware import LoggingMiddleware
from contextlib import asynccontextmanager

from fastapi import Response

import logging

from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST
)

ready = False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@asynccontextmanager
async def lifespan(app: FastAPI):

    global ready

    ready = True

    yield

    ready = False


app = FastAPI(
    lifespan=lifespan
)

app.add_middleware(LoggingMiddleware)

config = load_config("config.yaml")

@app.get("/")
def root():
    return {"message": "API Running"}


@app.post("/summarize",
          response_model=SummariseResponse)
def summarize(request: SummariseRequest):

    summary = generate_summary(
        request.text,
        request.style,
        config.llm.model,
        config.llm.max_tokens
    )

    return SummariseResponse(
        summary=summary,
        model=config.llm.model,
        input_chars=len(request.text)
    )

@app.get("/healthz")
def healthz():
    return {
        "status": "alive"
    }

@app.get("/readyz")
def readyz():

    if ready:
        return {
            "status": "ready"
        }

    return Response(
        content='{"status":"not_ready"}',
        status_code=503,
        media_type="application/json"
    )

@app.get("/metrics")
def metrics():

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )