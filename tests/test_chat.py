import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from Vitae.app.externalservices.openai.openai_api import OpenAIIntegrationError

client = TestClient(app)


@patch("Vitae.app.backend.routes.chat.send_message")
def test_chatsend_success(mock_send_message):

    mock_send_message.return_value = "Hello! I am ready to answer your questions."

    response = client.post(
        "/api/v1/chat/chatsend", json={"messages": [{"role": "user", "content": "Hi!"}]}
    )

    assert response.status_code == 200
    assert response.json() == {
        "role": "assistant",
        "content": "Hello! I am ready to answer your questions.",
    }


@patch("Vitae.app.backend.routes.chat.send_message")
def test_chatsend_fallback(mock_send_message):
    mock_send_message.side_effect = OpenAIIntegrationError("OpenAI API is down")

    response = client.post(
        "/api/v1/chat/chatsend",
        json={"messages": [{"role": "user", "content": "Tell me about your skills."}]},
    )

    assert response.status_code == 200
    assert "Vova.Spetcialny@gmail.com" in response.json()["content"]


def test_chatsend_validation_error():

    response = client.post("/api/v1/chat/chatsend", json={})

    assert response.status_code == 422
