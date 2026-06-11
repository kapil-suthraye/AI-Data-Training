from unittest.mock import patch

from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


# Test-1 Happy Style 
@patch("app.generate_summary")
def test_summarize_happy_path_with_mocked_llm(
    mock_generate_summary
):

    mock_generate_summary.return_value = (
        "Mocked summary"
    )

    response = client.post(
        "/summarize",
        json={
            "text":
            "Artificial intelligence is transforming industries by improving productivity and efficiency.",
            "style":
            "brief"
        }
    )

    assert response.status_code == 200

    assert (
        response.json()["summary"]
        == "Mocked summary"
    )

# Test-2 Invalid Endpoint
def test_summarize_invalid_style_returns_422():

    response = client.post(
        "/summarize",
        json={
            "text":
            "Artificial intelligence is transforming industries by improving productivity and efficiency.",
            "style":
            "unknown"
        }
    )

    assert response.status_code == 422

#Test-3 Health Endpoint
def test_healthz_returns_200_alive():

    response = client.get(
        "/healthz"
    )

    assert response.status_code == 200

    assert response.json() == {
        "status": "alive"
    }

