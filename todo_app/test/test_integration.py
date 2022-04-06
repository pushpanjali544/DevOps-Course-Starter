import pytest
from dotenv import find_dotenv, load_dotenv
from todo_app.app import create_app
from unittest.mock import patch, Mock
import os
import mongomock

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = create_app()
        # Use the app to create a test_client that can be used in our
        with test_app.test_client() as client:
            yield client

def test_index_page( client):
 # Replace call to requests.get(url) with our own function
   
    response = client.get('/')
    assert response.status_code==200





    

