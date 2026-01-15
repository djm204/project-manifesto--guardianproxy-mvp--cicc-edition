from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pii_scrub_ai_middleware.sanitizer.sentry_engine import sanitize_pii
import aioredis
import os

app = FastAPI()

@app.middleware("http")
async def dispatch(request: Request, call_next):
    if request.url.path == "/v1/chat/completions":
        body = await request.json()
        sanitized_prompt, token_mapping = sanitize_pii(body['prompt'])
        redis = await aioredis.from_url("redis://localhost")
        await redis.set(body['id'], token_mapping)
        body['prompt'] = sanitized_prompt
        request._body = body
    response = await call_next(request)
    if response.status_code == 200 and request.url.path == "/v1/chat/completions":
        body = response.body
        redis = await aioredis.from_url("redis://localhost")
        token_mapping = await redis.get(request.json()['id'])
        for token, pii in token_mapping.items():
            body = body.replace(token, pii)
        response.body = body
    return response