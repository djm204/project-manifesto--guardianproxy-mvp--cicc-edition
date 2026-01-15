import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy import vault_gateway

def test_vault_gateway():
    """Test that vault gateway functions correctly."""
    # Mock a request and response here, then test the gateway's functionality
    # Ensure the response is correctly anonymized and tokenized