import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sanitizer.sentry_engine import sanitize_pii

def test_sanitize_pii():
    """Test that sanitize_pii function works correctly."""
    text = "Hello, my name is John Doe. My SIN is 123 456 789."
    sanitized_text, token_mapping = sanitize_pii(text)
    assert token_mapping == {"{{CLIENT_1}}": "John Doe", "{{CLIENT_2}}": "123 456 789"}
    for original, token in token_mapping.items():
        assert original not in sanitized_text
        assert token in text