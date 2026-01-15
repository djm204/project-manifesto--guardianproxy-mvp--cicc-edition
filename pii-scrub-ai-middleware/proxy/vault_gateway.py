from fastapi import FastAPI, HTTPException
from fastapi.middleware import Middleware
from redis import Redis
from sanitizer.sentry_engine import sanitize_pii

app = FastAPI()

@app.post("/v1/chat/completions")
async def handle_request(request: dict):
    sanitized_text, token_mapping = sanitize_pii(request.text)
    Redis().set(request.id, token_mapping, ex=1800)
    try:
        response = await send_to_ollama(sanitized_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error sending request to Ollama")
    return rehydrate_response(response, Redis().get(request.id))