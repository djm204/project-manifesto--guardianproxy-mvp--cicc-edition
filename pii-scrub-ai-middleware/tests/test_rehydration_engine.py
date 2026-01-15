import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy.rehydration_engine import rehydrate

def test_rehydrate():
    """Test that rehydrate function works correctly."""
    response = {"text": "Hello, {{CLIENT_1}}. Your SIN is {{CLIENT_2}}."}
    mapping = {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"}
    expected_output = {"text": "Hello, John Doe. Your SIN is 123 456 789."}
    assert rehydrate(response, mapping) == expected_output