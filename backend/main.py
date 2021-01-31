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


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


if __name__ == "__main__":
    app.run()