from flask import Flask, request, jsonify
from flask_cors import CORS
from helpers.database import isInDatabase, getFromDatabase, getExistingTags
from helpers.youTube import getYoutubeVideos

app = Flask(__name__)
CORS(app)


@app.route("/search", methods=["POST"])
def search():
    response = "Nothing happened"
    search = request.form["q"]

    if isInDatabase(search):
        response = getFromDatabase(search)
    else:
        getYoutubeVideos(search)
        response = {str(search): "is not in the db"}

    return response


if __name__ == "__main__":
    app.run()