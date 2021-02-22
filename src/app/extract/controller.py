"""
    Endpoint controller layer of the project
"""
from flask import request, send_file
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from .data_access.db_operations import DBOperations
from .api_handler.api_handler import AudioOperationsHandler

API = Namespace("Extract", description="Extract API")


@API.route("/create_audio")
class CreateAudio(Resource):
    """
    Class handling HTTP requests to endpoint /create_audio
    """

    @classmethod
    def post(cls):
        """
        Post endpoint for the application
        """
        try:
            file_id, audio_file_type = AudioOperationsHandler.create_audio(request)
            return (
                {
                    "result": f"Audio Inserted, File ID: {file_id}, File Type: {audio_file_type}"
                },
                200,
            )
        except ValidationError as err:
            return {"result": str(err)}, 400


@API.route("/delete_audio/<audioFileType>/<audioFileID>")
class DeleteAudio(Resource):
    """
    Class handling HTTP requests to endpoint /delete_audio/<audioFileType>/<audioFileID>
    """

    @classmethod
    def delete(cls, audioFileType, audioFileID):
        """
        Delete endpoint for the application
        """
        try:
            if audioFileType not in ["song", "podcast", "audiobook"]:
                return {
                    "result": "Please pass audioFileType as song, podcast or audiobook."
                }, 400
            DBOperations.delete_from_db(
                audio_file_type=audioFileType, audio_file_id=audioFileID
            )
            return ({"result": "Audio Deleted Successfully."}, 200)
        except Exception as err:
            return {"result": str(err)}, 400


@API.route("/update_audio/<audioFileType>/<audioFileID>")
class UpdateAudio(Resource):
    """
    Class handling HTTP requests to endpoint /update_audio/<audioFileType>/<audioFileID>
    """

    @classmethod
    def put(cls, audioFileType, audioFileID):
        """
        Update endpoint for the application
        """
        try:
            AudioOperationsHandler.update_audio(audioFileType, audioFileID, request)
            return ({"result": "Updated Document for the required audioFileId."}, 200)
        except ValidationError as err:
            return {"result": str(err)}, 400


@API.route("/get_audio/<audioFileType>/<audioFileID>")
class GetAudioByID(Resource):
    """
    Class handling HTTP requests to endpoint /get_audio/<audioFileType>/<audioFileID>
    """

    @classmethod
    def get(cls, audioFileType, audioFileID):
        """
        Get endpoint for the application
        """
        try:
            document = AudioOperationsHandler.get_operation(audioFileType, audioFileID)
            return send_file(
                document, attachment_filename=document.filename, as_attachment=True
            )
        except ValidationError as err:
            return {"result": str(err)}, 400


@API.route("/get_audio/<audioFileType>")
class GetAudio(Resource):
    """
    Class handling HTTP requests to endpoint /get_audio/<audioFileType>
    """

    @classmethod
    def get(cls, audioFileType):
        """
        Get endpoint for the application
        """
        try:
            memory_file = AudioOperationsHandler.get_operation(audioFileType)
            return send_file(
                memory_file,
                attachment_filename=f"{audioFileType}s.zip",
                as_attachment=True,
            )
        except ValidationError as err:
            return {"result": str(err)}, 400
