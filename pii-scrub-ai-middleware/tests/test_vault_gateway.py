import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy.vault_gateway import process_request, process_response

def test_process_request():
    """Test that process_request function works correctly."""
    request = {"text": "Hello, my name is John Doe. My SIN is 123 456 789."}
    expected_output = {"text": "Hello, my name is {{CLIENT_1}}. My SIN is {{CLIENT_2}}."}
    assert process_request(request) == expected_output

def test_process_response():
    """Test that process_response function works correctly."""
    response = {"text": "Hello, {{CLIENT_1}}. Your SIN is {{CLIENT_2}}."}
    expected_output = {"text": "Hello, John Doe. Your SIN is 123 456 789."}
    assert process_response(response) == expected_output