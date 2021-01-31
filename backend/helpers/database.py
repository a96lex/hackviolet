import os
import pymysql
import json

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
        cursor.execute(
            "SELECT * FROM accepted_videos WHERE search = '{}'".format(str(search))
        )
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return True


def getFromDatabase(search):
    unix_socket = "/cloudsql/{}".format(db_connection_name)
    cnx = pymysql.connect(
        user=db_username,
        password=db_pass,
        unix_socket=unix_socket,
        db=db_accepted_videos,
    )
    with cnx.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM accepted_videos WHERE search = '{}'".format(str(search))
        )
        data = cursor.fetchall()

        if data is None:
            return "there is nothing here"
        else:
            return json.dumps(data)


def getExistingTags():
    tags = []
    while len(tags) < 10:
        tags.append("ii")
    return {"tags": tags}


def addToDb(video, search):
    v_id = video["link"]
    title = video["title"]
    views = video["viewCount"]["text"]
    search = str(search)
    video_thumbnail = video["thumbnails"][0]["url"]
    duration = video["duration"]
    channel = video["channel"]["name"]
    channel_thumbnail = video["channel"]["thumbnails"][0]["url"]

    unix_socket = "/cloudsql/{}".format(db_connection_name)

    cnx = pymysql.connect(
        user=db_username,
        password=db_pass,
        unix_socket=unix_socket,
        db=db_accepted_videos,
    )

    print(cnx)

    sql = "insert into accepted_videos(id,views,title,search,video_thumbnail,duration,channel,channel_thumbnail) values('{}',{},'{}','{}','{}','{}','{}','{}');".format(
        v_id,
        int(views[:-6].replace(",", "")),
        title,
        search,
        video_thumbnail,
        duration,
        channel,
        channel_thumbnail,
    )

    with cnx.cursor() as cursor:
        print(cursor)
        cursor.execute(sql)
        cnx.commit()
