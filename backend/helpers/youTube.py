from youtubesearchpython import VideosSearch
from .database import addToDb


def getYoutubeVideos(search):
    search = VideosSearch(search)

    response = search.result()["result"]

    count = 0

    while len(response) < 100 and count < 10:
        search.next()
        response += search.result()["result"]
        count += 1

    response = response[:1]

    for video in response:
        # if isFemale(video["link"]):
        addToDb(video, search)
        # else:
        #     continue
    return None
