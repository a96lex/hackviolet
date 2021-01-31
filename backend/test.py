from youtubesearchpython import VideosSearch

search = VideosSearch("Getting Started with Cloud SQL for MySQL")

response = search.result()["result"]

while len(response) < 10:
    search.next()
    response += search.result()["result"]

# id,views,title,search,video_thumbnail,duration,channel,channel_thumbnail
print(type(response[0]["link"]))
print(type(response[0]["viewCount"]["text"]))
print((response[0]["title"]))
search = search
print(type(response[0]["thumbnails"][0]["url"]))
print(type(response[0]["duration"]))
print(type(response[0]["channel"]["name"]))
print(type(response[0]["channel"]["thumbnails"][0]["url"]))