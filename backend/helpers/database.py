import os
import pymysql

db_username = os.environ.get("DB_USERNAME")
db_pass = os.environ.get("DB_PASS")
db_accepted_videos = os.environ.get("ACCEPTED_VIDEOS")
db_connection_name = os.environ.get("CONNECTION_NAME")
host = os.environ.get("HOST")


def isInDatabase(search):
    unix_socket = "/cloudsql/{}".format(db_connection_name)
    cnx = pymysql.connect(
        user=db_username,
        password=db_pass,
        unix_socket=unix_socket,
        db=db_accepted_videos,
    )
    with cnx.cursor() as cursor:
        cursor.execute("SELECT id FROM * WHERE search = " + str(search))
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return True


def getFromDatabase(search):
    return {str(search): "something"}


def getExistingTags():
    tags = []
    while len(tags) < 10:
        tags.append("ii")
    return {"tags": tags}
