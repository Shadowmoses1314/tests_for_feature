from fastapi.testclient import TestClient
from url_task import app

client = TestClient(app)


def test_encode_url_with_hash():
    url = "https://www.example.com/path/param=value"
    encoded_url = "https%3A%2F%2Fwww.example.com%2Fpath%2Fparam%3Dvalue"
    response = client.get(f"/encode_url/{url}")
    assert response.status_code == 200
    assert response.json() == {"encoded_url": f"url={encoded_url}"}
