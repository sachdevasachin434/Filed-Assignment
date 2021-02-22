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


#   Podcast Test Cases
#
def test_correct_input_with_audio_file_passed(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_with_audio_file_not_passed(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_podcast_name(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            # "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_duration(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            # "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_host(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            # "host":"cde",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_participants(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            # "participants":["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_participants(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            # "participants":["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_uploaddate(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            # "uploadDate": "06/02/22 00:00:00"
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_random_key_passed_into_audiofilemetadata(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
            "abc": "xyz",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search(
        "Only podcast_name, duration, uploadDate, host, participants are allowed as keys in audioFileMetaData.",
        data["result"],
    )
    assert status_code == 400


def test_wrong_podcast_id(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "30",
            "host": "cde",
            "participants": ["lmn", "opq"],
            # "uploadDate": "06/02/22 00:00:00"
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1001", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Audio with specified audioFileID doesn't exist.", data["result"])
    assert status_code == 400


def test_random_key_passed_into_audiofilemetadata(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "sample_voice",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
            "abc": "xyz",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search(
        "Only podcast_name, duration, uploadDate, host, participants are allowed as keys in audioFileMetaData.",
        data["result"],
    )
    assert status_code == 400


# Song Test Cases
#
def test_correct_input_with_audio_file_passed(client):
    data = {}
    data["audioFileMetaData"] = str({"song_name": "sample_voice", "duration": "30"})
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_audio_file(client):
    data = {}
    data["audioFileMetaData"] = str({"song_name": "sample_voice", "duration": "30"})
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_song_name(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            # "song_name": "sample_voice",
            "duration": "40"
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_duration(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "song_name": "sample_voice-2",
            # "duration": "40"
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


# AudioBook Test Cases
#
def test_correct_input_with_audio_file_passed(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "sample_voice",
            "duration": "30",
            "narrator": "abc",
            "author": "xyz",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_audio_file_passed(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "sample_voice",
            "duration": "30",
            "narrator": "abc",
            "author": "xyz",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_narrator(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "sample_voice",
            "duration": "30",
            # "narrator": "abc",
            "author": "xyz",
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_correct_input_without_author(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "sample_voice",
            "duration": "30",
            "narrator": "abc",
            # "author": "xyz"
        }
    )
    # data["audioFile"] = (io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"), 'test.mp3')
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


# General Test cases
#
def test_large_podcast_name(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "s" * 101,
            "duration": "2",
            "host": "abc",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass podcast_name", data["result"])
    assert status_code == 400


def test_large_host(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "h" * 101,
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass host", data["result"])
    assert status_code == 400


def test_many_participants(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn"] * 11,
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Participants can not be more that 10.", data["result"])
    assert status_code == 400


def test_large_participant_name(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn" * 101],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Participant name can not exceed 100 characters.", data["result"])
    assert status_code == 400


def test_negative_duration(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "-2",
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass duration", data["result"])
    assert status_code == 400


def test_past_upload_time(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06/02/20 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Upload Time can not be in the past.", data["result"])
    assert status_code == 400


def test_large_song_name(client):
    data = {}
    data["audioFileMetaData"] = str({"song_name": "s" * 101, "duration": "2"})
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass song_name", data["result"])
    assert status_code == 400


def test_large_book_title(client):
    data = {}
    data["audioFileMetaData"] = str(
        {"book_title": "s" * 101, "duration": "2", "narrator": "abc", "author": "xyz"}
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass book_title", data["result"])
    assert status_code == 400


def test_large_narrator(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "some_audio",
            "duration": "2",
            "narrator": "n" * 101,
            "author": "xyz",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass narrator", data["result"])
    assert status_code == 400


def test_large_author(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "book_title": "some_audio",
            "duration": "2",
            "narrator": "abc",
            "author": "a" * 101,
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass author", data["result"])
    assert status_code == 400


# Instance Test Cases
#
def test_wrong_podcast_name_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": 10,
            "duration": "2",
            "host": "abc",
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass podcast_name", data["result"])
    assert status_code == 400


def test_wrong_host_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": 10,
            "participants": ["lmn", "opq"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass host", data["result"])
    assert status_code == 400


def test_wrong_participants_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": "abc",
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass participants as a list.", data["result"])
    assert status_code == 400


def test_duration_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": 12,
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06/02/22 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Updated Document for the required audioFileId", data["result"])
    assert status_code == 200


def test_wrong_upload_time_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06-02-20 00:00:00",
        }
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/podcast/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search(
        "Please pass upload time in following format: dd/mm/yy HH:MM:SS", data["result"]
    )
    assert status_code == 400


def test_wrong_song_name_instance(client):
    data = {}
    data["audioFileMetaData"] = str({"song_name": 11, "duration": "2"})
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/song/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass song_name", data["result"])
    assert status_code == 400


def test_wrong_book_title_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {"book_title": 11, "duration": "2", "narrator": "abc", "author": "xyz"}
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass book_title", data["result"])
    assert status_code == 400


def test_wrong_narrator_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {"book_title": "some_audio", "duration": "2", "narrator": 11, "author": "xyz"}
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass narrator", data["result"])
    assert status_code == 400


def test_wrong_author_instance(client):
    data = {}
    data["audioFileMetaData"] = str(
        {"book_title": "some_audio", "duration": "2", "narrator": "abc", "author": 11}
    )
    data["audioFile"] = (
        io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01"),
        "test.mp3",
    )
    response = client.put(
        "/update_audio/audiobook/1", data=data, content_type="multipart/form-data"
    )
    data = response.json
    status_code = response.status_code
    assert search("Please pass author", data["result"])
    assert status_code == 400
