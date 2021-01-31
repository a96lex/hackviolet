from youtubesearchpython import VideosSearch

search = VideosSearch("Getting Started with Cloud SQL for MySQL")

response = search.result()["result"]

while len(response) < 10:
    search.next()
    response += search.result()["result"]

print(response[0])