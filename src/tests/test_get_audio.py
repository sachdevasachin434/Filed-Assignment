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


def test_with_audioid(client):
    response = client.get("/get_audio/song/1")
    data = response.data
    status_code = response.status_code
    assert data is not None
    assert isinstance(data, bytes)
    assert status_code == 200


def test_with_wrong_audioid(client):
    response = client.get("/get_audio/song/1111")
    data = response.json
    status_code = response.status_code
    assert search("Audio with specified audioFileID doesn't exist.", data["result"])
    assert status_code == 400


def test_without_audioid(client):
    response = client.get("/get_audio/song")
    data = response.data
    status_code = response.status_code
    assert data is not None
    assert status_code == 200


## Should be test seperately when no data is there in database.
# def test_with_no_data_for_audiotype(client):
#     response = client.get("/get_audio/audiobook")
#     data = response.data
#     status_code = response.status_code
#     assert search("No audio file found for audioFileType:", data[result])
#     assert status_code == 400


def test_wrong_audiotype(client):
    response = client.get("/get_audio/abc")
    data = response.json
    status_code = response.status_code
    assert search(
        "Please pass audioFileType as song, podcast or audiobook.", data["result"]
    )
    assert status_code == 400
