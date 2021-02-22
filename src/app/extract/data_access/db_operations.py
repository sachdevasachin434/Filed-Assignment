"""
    Database Layer of the project.
"""

from marshmallow import ValidationError
from ...utils import connection

mydb, file_storage = connection()


class DBOperations:
    """
    Class that contains method to load data to mongodb server.
    """

    @staticmethod
    def next_sequence(audio_file_type):
        """Function that return autoincremented sequence value.

        Args:
            audio_file_type (string): One among [song, podcast, audiobook]

        Returns:
            Int: Incremented value of the sequence for passed audio_file_type.
        """
        sequence_data = mydb["SequenceCollection"].find_and_modify(
            query={"Name": audio_file_type},
            update={"$inc": {"Value": 1}},
            new=True,
            upsert=True,
        )
        return sequence_data["Value"]

    @staticmethod
    def insert_into_db(audio_file_type, data, audio_file):
        """Acts as database function for /create_audio and inserts metadata \
            and audio_file to MongoDB and gridfs respectively.

        Args:
            audio_file_type (string): One among [song, podcast, audiobook]
            data (dict): {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06/02/20 00:00:00",
        }
            audio_file (FileStorage): Audio File that is passed as form parameter.

        Raises:
            Exception: Any Exception that is raised by MongoDB or Gridfs.

        Returns:
            Int: Id of newly created MongoDB document.
        """
        try:
            # set collection for inserting data.
            if audio_file_type == "song":
                datacol = mydb["SongData"]
            if audio_file_type == "podcast":
                datacol = mydb["PodcastData"]
            if audio_file_type == "audiobook":
                datacol = mydb["AudiobookData"]

            document_id = DBOperations.next_sequence(audio_file_type)

            audio_id = file_storage.put(
                audio_file,
                filename=audio_file.filename,
                content_type=audio_file.content_type,
            )

            data["audio_id"] = audio_id
            # Using insert_one method to create and insert a document.
            datacol.insert_one({**{"_id": document_id}, **data})

            return document_id
        except Exception:
            raise Exception

    @staticmethod
    def delete_from_db(audio_file_type, audio_file_id):
        """Acts as a database function for /delete_audio/<audioFileType>/<audioFileID>\
             and deletes document, file and clusters from MongoDB and Gridfs.

        Args:
            audio_file_type (string): Can be among song, podcast and audiofile.
            audio_file_id (string): Id for which data needs to be deleted which is\
                 passed as a path parameter.

        Raises:
            ValidationError: If no data is found for passed audio_file_id then \
                raises the validation error.
        """
        if audio_file_type == "song":
            datacol = mydb["SongData"]
        if audio_file_type == "podcast":
            datacol = mydb["PodcastData"]
        if audio_file_type == "audiobook":
            datacol = mydb["AudiobookData"]
        if not datacol.find({"_id": int(audio_file_id)}).count():
            raise ValidationError("Audio with specified audioFileID doesn't exist.")

        for document in datacol.find({"_id": int(audio_file_id)}):
            file_storage.delete(document["audio_id"])
        datacol.remove({"_id": int(audio_file_id)})

    @staticmethod
    def update_db(audio_file_type, data, audio_file=None):
        """Acts as a database function for /update_audio/<audioFileType>/<audioFileID>\
             and updates document, file and clusters from MongoDB and Gridfs.

        Args:
            audio_file_type (string): Can be among song, podcast and audiofile.
            data ([type]): {
            "podcast_name": "some_audio",
            "duration": "2",
            "host": "abc",
            "participants": ["lmn"],
            "uploadDate": "06/02/20 00:00:00",
        }
            audio_file (FileStorage, optional): Audio File that is passed as form \
                parameter. Defaults to None.

        Raises:
            ValidationError: If no data is found for passed audio_file_id then\
                 raises the validation error.
        """
        if audio_file_type == "song":
            datacol = mydb["SongData"]
        if audio_file_type == "podcast":
            datacol = mydb["PodcastData"]
        if audio_file_type == "audiobook":
            datacol = mydb["AudiobookData"]
        if not datacol.find({"_id": data["id"]}).count():
            raise ValidationError("Audio with specified audioFileID doesn't exist.")
        if audio_file:
            for document in datacol.find({"_id": data["id"]}):
                file_storage.delete(document["audio_id"])
            audio_id = file_storage.put(audio_file, filename=audio_file.filename)
            data["audio_id"] = audio_id
        document_id = data["id"]
        del data["id"]
        datacol.update({"_id": document_id}, {"$set": data})

    @staticmethod
    def get_info(audio_file_type, audio_file_id=None):
        """Acts as a database function for /get_audio/<audioFileType>/<audioFileID>\
             and /get_audio/<audioFileType> and returns GridFS files.

        Args:
            audio_file_type (string): Can be among song, podcast and audiofile.
            audio_file_id (string, optional): Id for which file audio file is \
                required. Defaults to None.

        Returns:
            List or GridFS Object: If audio_file_id --> returns GridFS. \
                Else --> List of GridFS objects.
        """
        if audio_file_type == "song":
            datacol = mydb["SongData"]
        if audio_file_type == "podcast":
            datacol = mydb["PodcastData"]
        if audio_file_type == "audiobook":
            datacol = mydb["AudiobookData"]

        if audio_file_id is None:
            document_collection = []
            if not datacol.find().count():
                raise ValidationError(
                    f"No audio file found for audioFileType: {audio_file_type}"
                )
            for document in datacol.find():
                document_collection.append(file_storage.get(document["audio_id"]))
            return document_collection
        if not datacol.find({"_id": int(audio_file_id)}).count():
            raise ValidationError("Audio with specified audioFileID doesn't exist.")
        for document in datacol.find({"_id": int(audio_file_id)}):
            return file_storage.get(document["audio_id"])
