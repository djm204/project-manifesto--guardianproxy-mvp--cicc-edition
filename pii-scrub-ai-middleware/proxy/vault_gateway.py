from fastapi import FastAPI, Request
from redis import Redis
import sanitizer

app = FastAPI()
redis = Redis(host='localhost', port=6379, db=0)

@app.middleware("http")
async def sanitize_middleware(request: Request, call_next):
    """FastAPI middleware to sanitize PII from the request."""
    sanitized_text, token_mapping = sanitizer.sanitize_pii(request.body())
    
    key = request.headers.get('X-Request-ID')
    redis.set(key, token_mapping, ex=1800)
    
    request._body = sanitized_text
    response = await call_next(request)
    
    token_mapping = redis.get(key)
    for token, pii in token_mapping.items():
        response.body = response.body.replace(token, pii)
    
    return response