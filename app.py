
from flask import Flask, make_response

app = Flask(__name__)

# Добавляем CORS-заголовок для всех маршрутов
@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/", methods=["GET"])
def index():
    response = make_response("st3pa")
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    return response


@app.route("/login/", methods=["GET"])
def login():
    response = make_response("st3pa")
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    return response


@app.route("/promise/", methods=["GET"])
def promise():
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


@app.route("/fetch/", methods=["GET"])
def fetch_page():
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
                const result = await response.text();
                inp.value = result;
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