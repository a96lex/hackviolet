def parseVideo(video):
    v_id = video["link"]
    title = video["title"]
    views = video["viewCount"]["text"]
    search = str(search)
    video_thumbnail = video["thumbnails"][0]["url"]
    duration = video["duration"]
    channel = video["channel"]["name"]
    channel_thumbnail = video["channel"]["thumbnails"][0]["url"]

    return tuple(
        v_id,
        int(views[:-6].replace(",", "")),
        title,
        search,
        video_thumbnail,
        duration,
        channel,
        channel_thumbnail,
    )