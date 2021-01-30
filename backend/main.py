from flask import Flask, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    data = request.get_json()
    return {"query": data}


app.run()

# from flask import Flask, jsonify


# app = Flask(__name__)
# container = ["Hello World!", "Google"]


# @app.route("/mainpage/")
# def mainpage():
#     return jsonify(container)


# @app.route("/get/<number>")
# def get(number):
#     if int(number) > len(container):
#         return "That number is greater than the size of the container"
#     else:
#         return jsonify(container[int(number)])


# @app.route("/post/<word>")
# def post(word):
#     container.append(word)
#     return jsonify(word)
