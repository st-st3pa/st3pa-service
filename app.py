 
from flask import Flask, make_response, request
import json

app = Flask(__name__)


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = (
        "GET,POST,PUT,DELETE,OPTIONS"
    )
    response.headers["Access-Control-Allow-Headers"] = (
        "x-test,ngrok-skip-browser-warning,Content-Type,Accept,"
        "Access-Control-Allow-Headers"
    )
    return response


@app.route("/", defaults={"path": ""}, methods=[
    "GET", "POST", "PUT", "DELETE", "OPTIONS"
])
@app.route("/<path:path>", methods=[
    "GET", "POST", "PUT", "DELETE", "OPTIONS"
])
def routes(path):
    path = path.rstrip("/")
    if path == "":
        return make_response("st3pa")

    if path == "login":
        response = make_response("st3pa")
        response.headers["Content-Type"] = "text/plain; charset=UTF-8"
        return response

    if path == "promise":
        code = """function task(x) {
    return new Promise((resolve, reject) => {
        if (x < 18) {
            resolve('yes');
        } else {
            reject('no');
        }
    });
}"""
        response = make_response(code)
        response.headers["Content-Type"] = "text/plain; charset=UTF-8"
        return response

    if path == "fetch":
        html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Fetch</title>
</head>
<body>
<input id="inp" type="text">
<button id="bt" type="button">Fetch</button>
<script>
document.getElementById('bt').addEventListener('click', async () => {
    const inp = document.getElementById('inp');
    try {
        const response = await fetch(inp.value);
        inp.value = await response.text();
    } catch (error) {
        inp.value = 'Error: ' + error.message;
    }
});
</script>
</body>
</html>"""
        response = make_response(html)
        response.headers["Content-Type"] = "text/html; charset=UTF-8"
        return response

    if path.rstrip("/") == "result4":
        result = {
            "message": "st3pa",
            "x-result": request.headers.get("x-test"),
            "x-body": request.get_data(as_text=True)
        }
        response = make_response(json.dumps(result), 200)
        response.headers["Content-Type"] = "application/json"
        return response

    return make_response("PATH RECEIVED: " + repr(path), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
