from youtubesearchpython import VideosSearch

search = VideosSearch("Fortran")

response = search.result()["result"]

while len(response) < 10:
    search.next()
    response += search.result()["result"]

print(response[1]["link"])