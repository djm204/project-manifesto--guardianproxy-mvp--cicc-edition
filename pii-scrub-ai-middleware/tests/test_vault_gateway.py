import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy.vault_gateway import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_vault_gateway():
    """Test the vault_gateway FastAPI app."""
    response = client.post("/v1/chat/completions", headers={"X-Request-ID": "1"}, data="Hello, my name is John Doe. My SIN is 123 456 789.")
    assert response.status_code == 200
    assert "Hello, my name is John Doe. My SIN is 123 456 789." in response.text