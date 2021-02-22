"""
    API Handler Layer for handling request params.
"""
import time
import zipfile
import ast
from io import BytesIO
from marshmallow import ValidationError
from .. import validators as validator
from ..data_access.db_operations import DBOperations



class AudioOperationsHandler:
    """
    Class to handle request validation and python level manipulation.
    """

    @staticmethod
    def create_audio(request):
        """Method to make required data arrangements for audio creation.

        Args:
            request (request): request containing file type, audio file and meta data as parameters.

        Returns:
            Int: ID of MongoDB Document.
        """
        validate = validator.AudioSchema()

        if (
            "audioFileType" not in request.form.keys()
            or "audioFileMetaData" not in request.form.keys()
        ):
            raise ValidationError(
                "Wrong Input: Please pass audioFileType and audioFileMetaData as form parameter."
            )
        if "audioFile" not in request.files.keys():
            raise ValidationError("Wrong Input: Please pass audioFile as param.")

        audio_file_type = request.form["audioFileType"]
        audio_file_meta_data = ast.literal_eval(request.form["audioFileMetaData"])
        data = {
            "audioFileType": audio_file_type,
            "audioFileMetaData": audio_file_meta_data,
        }
        data = validate.validate_input(dict(data))
        del data["audioFileType"]
        for key, value in data["audioFileMetaData"].items():
            data[key] = value
        del data["audioFileMetaData"]
        audio_file = request.files["audioFile"]
        file_id = DBOperations.insert_into_db(audio_file_type, data, audio_file)
        return file_id, audio_file_type

    @staticmethod
    def update_audio(audioFileType, audioFileID, request):
        """Method to make required data arrangements for audio or metadata updation.

        Args:
            request (request): request containing file type, audio file and meta data as parameters.
        """
        validate = validator.AudioUpdateSchema()
        if audioFileID is None or audioFileType is None:
            raise ValidationError(
                "Please pass audioFileType and audioFileId as Path Parameters"
            )

        if "audioFileMetaData" not in request.form.keys():
            raise ValidationError(
                "Please pass audioFileMetaData as form parameters for update operation"
            )

        data = {
            "audioFileType": audioFileType,
            "audioFileMetaData": ast.literal_eval(request.form["audioFileMetaData"]),
            "id": int(audioFileID),
        }
        data = validate.validate_input(dict(data))
        del data["audioFileType"]
        for key, value in data["audioFileMetaData"].items():
            data[key] = value
        del data["audioFileMetaData"]
        if "audioFile" in request.files.keys():
            audio_file = request.files["audioFile"]
            DBOperations.update_db(audioFileType, data, audio_file)
        else:
            DBOperations.update_db(audioFileType, data)

    @staticmethod
    def get_operation(audioFileType, audioFileID=None):
        """Function to call database and prepare required zip file.

        Args:
            audioFileType (string): One among [song, podcast, audiobook]

        Returns:
            BytesIO: Zip file containing all files of a certain audioFileType.
        """
        if audioFileType not in ["song", "podcast", "audiobook"]:
            raise ValidationError(
                "Please pass audioFileType as song, podcast or audiobook."
            )
        documents = DBOperations.get_info(audioFileType, audioFileID)

        if isinstance(documents, list):
            memory_file = BytesIO()
            with zipfile.ZipFile(memory_file, "w") as zipf:
                for individualFile in documents:
                    data = zipfile.ZipInfo(individualFile.filename)
                    data.date_time = time.localtime(time.time())[:6]
                    data.compress_type = zipfile.ZIP_DEFLATED
                    zipf.writestr(data, individualFile.read())
            memory_file.seek(0)
            return memory_file
        return documents
