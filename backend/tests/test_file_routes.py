import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import based on your app's structure

client = TestClient(app)

@pytest.fixture
def sample_file():
    # Create a sample file for testing
    return {"filename": "test.txt", "content": "This is a test file."}

def test_upload_file(sample_file):
    response = client.post(
        "/files/upload",
        files={"file": (sample_file["filename"], sample_file["content"])},
    )
    assert response.status_code == 200
    assert "file_id" in response.json()  # Adjust based on your response structure

def test_download_file():
    # First, upload a file to get its ID
    upload_response = client.post(
        "/files/upload",
        files={"file": ("test.txt", b"This is a test file.")},
    )
    file_id = upload_response.json()["file_id"]

    # Now test downloading the file
    response = client.get(f"/files/download/{file_id}")
    assert response.status_code == 200
    assert response.content == b"This is a test file."  # Adjust based on your file content

def test_download_nonexistent_file():
    response = client.get("/files/download/nonexistent_id")
    assert response.status_code == 404  # Adjust based on your error handling

