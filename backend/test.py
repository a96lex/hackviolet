from youtubesearchpython import VideosSearch

search = VideosSearch("Fortran")

response = search.result()["result"]

while len(response) < 100:
    search.next()
    response += search.result()["result"]

print(len(response[:100]))
