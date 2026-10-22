
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/login/", methods=["GET"])
def login():
    response = make_response("st3pa")
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/sample/", methods=["GET"])
def sample():
    code = "function task(x) { return x * this * this; }"
    response = make_response(code)
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/", methods=["GET"])
def index():
    response = make_response("st3pa")
    response.headers["X-Author"] = "st3pa"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response