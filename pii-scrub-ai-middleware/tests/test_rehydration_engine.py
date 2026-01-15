import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sanitizer import rehydrate

def test_rehydrate():
    """Test that rehydrate function works correctly."""
    # Create a mock masked string, token mapping, and expected output
    masked_string = "Hello, my name is {{CLIENT_1}}. My SIN is {{CLIENT_2}}."
    token_mapping = {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"}
    expected_output = "Hello, my name is John Doe. My SIN is 123 456 789."
    assert rehydrate(masked_string, token_mapping) == expected_output