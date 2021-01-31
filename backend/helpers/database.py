import os
import pymysql

db_username = os.environ.get("DB_USERNAME")
db_pass = os.environ.get("DB_PASS")
db_accepted_videos = os.environ.get("ACCEPTED_VIDEOS")
db_connexion_name = os.environ.get("CONNEXION_NAME")
host = os.environ.get("HOST")


def isInDatabase(search):

    cnx = pymysql.connect(
        user=db_username, password=db_pass, host=host, db=db_accepted_videos
    )
    with cnx.cursor() as cursor:
        cursor.execute("SELECT id FROM * WHERE search = ?", (search,))
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
