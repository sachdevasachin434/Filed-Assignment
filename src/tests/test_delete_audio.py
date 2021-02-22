import json
import pytest
import io
from flask import Flask
from ..main import app
from re import search


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# def test_correct_input(client):
#     response = client.delete("/delete_audio/podcast/20")
#     data = response.json
#     status_code = response.status_code
#     assert search("Audio Deleted Successfully.", data['result'])
#     assert status_code == 200


def test_wrong_audiofiletype(client):
    response = client.delete("/delete_audio/abc/1")
    data = response.json
    status_code = response.status_code
    assert search(
        "Please pass audioFileType as song, podcast or audiobook.", data["result"]
    )
    assert status_code == 400


def test_wrong_audiofileid(client):
    response = client.delete("/delete_audio/podcast/100000")
    data = response.json
    status_code = response.status_code
    assert search("Audio with specified audioFileID doesn't exist.", data["result"])
    assert status_code == 400
