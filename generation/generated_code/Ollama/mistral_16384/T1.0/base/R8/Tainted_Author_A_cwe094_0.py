from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers.get("file_contents", None)

    if data is not None:
        start = data.find("{") + 1
        end = len(data) - data[-1:] * 3 - data[:-start]
        content = data[start:end]

    return eval(content)
