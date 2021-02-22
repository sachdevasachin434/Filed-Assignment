"""
    HTTP argument validation
"""
from datetime import datetime
from marshmallow import ValidationError


class AudioSchema:
    """
    Class to validate input parameters for post api.
    """
    def validate_input(self, data):
        """Method to validate input parameter of post api.

        Args:
            data (dict): {
            "audioFileType": "podcast",
            "audioFileMetaData": {
                "podcast_name": "some_audio",
                "duration": "2",
                "host": "abc",
                "participants": ["lmn"],
                "uploadDate": "06/02/20 00:00:00",
            }
        }

        Raises:
            ValidationError: Any validation error that arrises in the data.

        Returns:
            dict: If all validation passed return the original data.
        """
        if "audioFileType" not in data or not isinstance(data["audioFileType"], str):
            raise ValidationError("Please pass audioFileType(:string) field in data.")
        if "audioFileMetaData" not in data or not isinstance(
            data["audioFileMetaData"], dict
        ):
            raise ValidationError(
                "Please pass audioFileMetaData(:dictionary) field in data."
            )
        if data["audioFileType"] not in ["song", "podcast", "audiobook"]:
            raise ValidationError(
                "Please pass audioFileType as song, podcast, or audiobook."
            )

        # Song Validation.
        if data["audioFileType"] == "song":
            if (
                "song_name" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["song_name"], str)
                or len(data["audioFileMetaData"]["song_name"]) > 100
            ):
                raise ValidationError(
                    "Please pass song_name(:string(max length = 100)) to create audio file."
                )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["song_name", "duration", "uploadDate"])
            ):
                raise ValidationError(
                    "Only song_name, duration, uploadDate are allowed as keys in audioFileMetaData."
                )

        # Podcast Validation.
        if data["audioFileType"] == "podcast":
            if (
                "podcast_name" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["podcast_name"], str)
                or len(data["audioFileMetaData"]["podcast_name"]) > 100
            ):
                raise ValidationError(
                    "Please pass podcast_name(:string(max length = 100)) to create audio file."
                )
            if (
                "host" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["host"], str)
                or len(data["audioFileMetaData"]["host"]) > 100
            ):
                raise ValidationError(
                    "Please pass host(:string(max length = 100)) to create audio file."
                )
            if "participants" in data["audioFileMetaData"].keys():
                if not isinstance(data["audioFileMetaData"]["participants"], list):
                    raise ValidationError("Please pass participants as a list.")
                if len(data["audioFileMetaData"]["participants"]) > 10:
                    raise ValidationError("Participants can not be more that 10.")
                for i in data["audioFileMetaData"]["participants"]:
                    if len(i) > 100:
                        raise ValidationError(
                            "Participant name can not exceed 100 characters."
                        )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["podcast_name", "duration", "uploadDate", "host", "participants"])
            ):
                raise ValidationError(
                    "Only podcast_name, duration, uploadDate, host, participants are "
                    "allowed as keys in audioFileMetaData."
                )

        # Audio Book Files.
        if data["audioFileType"] == "audiobook":
            if (
                "book_title" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["book_title"], str)
                or len(data["audioFileMetaData"]["book_title"]) > 100
            ):
                raise ValidationError(
                    "Please pass book_title(:string(max length = 100)) to create audio file."
                )
            if (
                "author" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["author"], str)
                or len(data["audioFileMetaData"]["author"]) > 100
            ):
                raise ValidationError(
                    "Please pass author(:string(max length = 100)) to create audio file."
                )
            if (
                "narrator" not in data["audioFileMetaData"].keys()
                or not isinstance(data["audioFileMetaData"]["narrator"], str)
                or len(data["audioFileMetaData"]["narrator"]) > 100
            ):
                raise ValidationError(
                    "Please pass narrator(:string(max length = 100)) to create audio file."
                )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["book_title", "duration", "uploadDate", "author", "narrator"])
            ):
                raise ValidationError(
                    "Only book_title, duration, uploadDate, author, narrator are "
                    "allowed as keys in audioFileMetaData."
                )

        # Comman Fields.
        if "duration" not in data["audioFileMetaData"].keys():
            raise ValidationError(
                "Please pass duration(:positive integer) for audio file."
            )
        if "duration" in data["audioFileMetaData"].keys():
            try:
                data["audioFileMetaData"]["duration"] = int(
                    data["audioFileMetaData"]["duration"]
                )
                if data["audioFileMetaData"]["duration"] < 0:
                    raise ValidationError(
                        "Please pass duration(:positive integer) for audio file."
                    )
            except:
                raise ValidationError(
                    "Please pass duration(:positive integer) of audio file."
                )
        if "uploadDate" not in data["audioFileMetaData"].keys():
            data["audioFileMetaData"]["uploadDate"] = datetime.now()
        else:
            try:
                data["audioFileMetaData"]["uploadDate"] = datetime.strptime(
                    data["audioFileMetaData"]["uploadDate"], "%d/%m/%y %H:%M:%S"
                )
            except:
                raise ValidationError(
                    "Please pass upload time in following format: dd/mm/yy HH:MM:SS"
                )
            if data["audioFileMetaData"]["uploadDate"] < datetime.now():
                raise ValidationError("Upload Time can not be in the past.")
        return data


class AudioUpdateSchema:
    """
    Class to validate input parameters for update api.
    """
    def validate_input(self, data):
        """Method to validate input parameter of update api.

        Args:
            data (dict): {
            "audioFileType": "podcast",
            "audioFileMetaData": {
                "podcast_name": "some_audio",
                "duration": "2",
                "host": "abc",
                "participants": ["lmn"],
                "uploadDate": "06/02/20 00:00:00",
            }
        }

        Raises:
            ValidationError: Any validation error that arrises in the data.

        Returns:
            dict: If all validation passed return the original data.
        """
        if "audioFileType" not in data or not isinstance(data["audioFileType"], str):
            raise ValidationError("Please pass audioFileType(:string) field in data.")
        if "audioFileMetaData" not in data or not isinstance(
            data["audioFileMetaData"], dict
        ):
            raise ValidationError(
                "Please pass audioFileMetaData(:dictionary) field in data."
            )
        if data["audioFileType"] not in ["song", "podcast", "audiobook"]:
            raise ValidationError(
                "Please pass audioFileType as song, podcast, or audiobook."
            )

        # Song Validation.
        if data["audioFileType"] == "song":
            if "song_name" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["song_name"], str)
                    or len(data["audioFileMetaData"]["song_name"]) > 100
                ):
                    raise ValidationError(
                        "Please pass song_name(:string(max length = 100)) to create audio file."
                    )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["song_name", "duration", "uploadDate"])
            ):
                raise ValidationError(
                    "Only song_name, duration, uploadDate are allowed as keys in audioFileMetaData."
                )

        # Podcast Validation.
        if data["audioFileType"] == "podcast":
            if "podcast_name" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["podcast_name"], str)
                    or len(data["audioFileMetaData"]["podcast_name"]) > 100
                ):
                    raise ValidationError(
                        "Please pass podcast_name(:string(max length = 100)) to create audio file."
                    )
            if "host" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["host"], str)
                    or len(data["audioFileMetaData"]["host"]) > 100
                ):
                    raise ValidationError(
                        "Please pass host(:string(max length = 100)) to create audio file."
                    )
            if "participants" in data["audioFileMetaData"].keys():
                if not isinstance(data["audioFileMetaData"]["participants"], list):
                    raise ValidationError("Please pass participants as a list.")
                if len(data["audioFileMetaData"]["participants"]) > 10:
                    raise ValidationError("Participants can not be more that 10.")
                for i in data["audioFileMetaData"]["participants"]:
                    if len(i) > 100:
                        raise ValidationError(
                            "Participant name can not exceed 100 characters."
                        )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["podcast_name", "duration", "uploadDate", "host", "participants"])
            ):
                raise ValidationError(
                    "Only podcast_name, duration, uploadDate, host, participants are "
                    "allowed as keys in audioFileMetaData."
                )

        # Audio Book Files.
        if data["audioFileType"] == "audiobook":
            if "book_title" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["book_title"], str)
                    or len(data["audioFileMetaData"]["book_title"]) > 100
                ):
                    raise ValidationError(
                        "Please pass book_title(:string(max length = 100)) to create audio file."
                    )
            if "author" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["author"], str)
                    or len(data["audioFileMetaData"]["author"]) > 100
                ):
                    raise ValidationError(
                        "Please pass author(:string(max length = 100)) to create audio file."
                    )
            if "narrator" in data["audioFileMetaData"].keys():
                if (
                    not isinstance(data["audioFileMetaData"]["narrator"], str)
                    or len(data["audioFileMetaData"]["narrator"]) > 100
                ):
                    raise ValidationError(
                        "Please pass narrator(:string(max length = 100)) to create audio file."
                    )
            if not set(data["audioFileMetaData"].keys()).issubset(
                set(["book_title", "duration", "uploadDate", "author", "narrator"])
            ):
                raise ValidationError(
                    "Only book_title, duration, uploadDate, author, narrator are "
                        "allowed as keys in audioFileMetaData."
                )

        # Comman Fields.
        if "duration" in data["audioFileMetaData"].keys():
            try:
                data["audioFileMetaData"]["duration"] = int(
                    data["audioFileMetaData"]["duration"]
                )
                if data["audioFileMetaData"]["duration"] < 0:
                    raise ValidationError(
                        "Please pass duration(:positive integer) for audio file."
                    )
            except:
                raise ValidationError(
                    "Please pass duration(:positive integer) of audio file."
                )

        if "uploadDate" in data["audioFileMetaData"].keys():
            try:
                data["audioFileMetaData"]["uploadDate"] = datetime.strptime(
                    data["audioFileMetaData"]["uploadDate"], "%d/%m/%y %H:%M:%S"
                )
            except:
                raise ValidationError(
                    "Please pass upload time in following format: dd/mm/yy HH:MM:SS"
                )
            if data["audioFileMetaData"]["uploadDate"] < datetime.now():
                raise ValidationError("Upload Time can not be in the past.")
        return data
