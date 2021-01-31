from youtubesearchpython import VideosSearch


def getYoutubeVideos(search):
    search = VideosSearch(search)

    response = search.result()["result"]

    count = 0

    while len(response) < 100 and count < 10:
        search.next()
        response += search.result()["result"]
        count += 1

    return response[:100]
