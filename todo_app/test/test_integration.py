import pytest
from dotenv import find_dotenv, load_dotenv
from todo_app.app import create_app
from unittest.mock import patch, Mock
import os

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our
    with test_app.test_client() as client:
        yield client

@patch('requests.request')
def test_index_page(mock_get_requests, client):
 # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')
    assert response.status_code==200
def mock_get_lists(Method ,url, params):
    if url ==  f"https://api.trello.com/1/boards/{os.getenv('BOARDID')}/cards":
        response = Mock()
# sample_trello_lists_response should point to some test response data
        sample_trello_lists_response=[{'id':'abcd','name':'test','idList':'fakeTODO'}]
        response.json.return_value = sample_trello_lists_response
        return response
    return None
