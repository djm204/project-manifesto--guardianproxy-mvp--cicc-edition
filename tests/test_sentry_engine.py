import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sanitizer.sentry_engine import sanitize_pii

def test_sanitize_pii():
    """Test that sanitize_pii function works correctly."""
    input_text = "Hello, my name is John Doe. My SIN is 123 456 789."
    expected_output = ("Hello, my name is {{CLIENT_1}}. My SIN is {{CLIENT_2}}.", 
                       {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"})
    assert sanitize_pii(input_text) == expected_output