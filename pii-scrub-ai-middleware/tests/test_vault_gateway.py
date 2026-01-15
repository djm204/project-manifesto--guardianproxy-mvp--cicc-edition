import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy import vault_gateway

def test_process_request():
    """Test that process_request function works correctly."""
    input_text = "Hello, my name is John Doe. My SIN is 123 456 789."
    expected_output = ("Hello, my name is {{CLIENT_1}}. My SIN is {{CLIENT_2}}.", {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"})
    assert vault_gateway.process_request(input_text) == expected_output

def test_process_response():
    """Test that process_response function works correctly."""
    input_text = {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"}
    expected_output = "Hello, my name is John Doe. My SIN is 123 456 789."
    assert vault_gateway.process_response(input_text) == expected_output