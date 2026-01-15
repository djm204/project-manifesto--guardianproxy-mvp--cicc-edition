import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from proxy import process_request, process_response

def test_process_request():
    """Test that process_request function works correctly."""
    # Create a mock request and expected output
    mock_request = {"data": "mock_request_data"}
    expected_output = {"data": "processed_mock_request_data"}
    assert process_request(mock_request) == expected_output

def test_process_response():
    """Test that process_response function works correctly."""
    # Create a mock response and expected output
    mock_response = {"data": "mock_response_data"}
    expected_output = {"data": "de-masked_mock_response_data"}
    assert process_response(mock_response) == expected_output