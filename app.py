
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "HEAD", "OPTIONS"])
def index():
    response = make_response("st3pa")
    response.headers["X-Author"] = "st3pa"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response