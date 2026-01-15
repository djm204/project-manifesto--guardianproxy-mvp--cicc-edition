import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from pii_scrub_ai_middleware.proxy.vault_gateway import app

client = TestClient(app)

def test_vault_gateway():
    """Test that vault_gateway works correctly."""
    response = client.post("/v1/chat/completions", json={"id": "1", "prompt": "Hello, my name is John Doe. My SIN is 123 456 789."})
    assert response.status_code == 200
    assert "Hello, my name is John Doe. My SIN is 123 456 789." in response.json()['text']