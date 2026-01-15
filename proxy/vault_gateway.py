from fastapi import FastAPI, Request
from redis import Redis

from sanitizer import sentry_engine

app = FastAPI()

@app.middleware("http")
async def sanitize_pii(request: Request, call_next):
    # Get raw request body
    raw_body = await request.json()

    # Sanitize PII from the raw request body
    sanitized_body, token_mapping = sentry_engine.sanitize_pii(raw_body)

    # Store the token mapping in Redis
    redis_client = Redis(host='localhost', port=6379, db=0)
    redis_client.set(request.headers['x-request-id'], token_mapping)

    # Create a new request with the sanitized body
    sanitized_request = Request(request.scope, request.receive)
    sanitized_request._body = sanitized_body

    response = await call_next(sanitized_request)

    return response