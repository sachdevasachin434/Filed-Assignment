"""
Utility function for the application.
"""
import pymongo
import gridfs


def connection():
    """Function that connects to mongodb database and return pymongo and gridfs object.

    Returns:
        [pymongo]: [mongodb object]
        [gridfs]: [gridfs object]
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["FiledDatabase"]

    file_storage = gridfs.GridFS(mydb)
    return mydb, file_storage
