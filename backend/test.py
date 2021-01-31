from youtubesearchpython import VideosSearch

search = VideosSearch("Getting Started with Cloud SQL for MySQL")

response = search.result()["result"]

while len(response) < 10:
    search.next()
    response += search.result()["result"]

# id,views,title,search,video_thumbnail,duration,channel,channel_thumbnail
print((response[0]["link"]))
print((response[0]["viewCount"]["text"]))
print((response[0]["title"]))
print(str("Cloud SQL"))
print((response[0]["thumbnails"][0]["url"]))
print((response[0]["duration"]))
print((response[0]["channel"]["name"]))
print((response[0]["channel"]["thumbnails"][0]["url"]))