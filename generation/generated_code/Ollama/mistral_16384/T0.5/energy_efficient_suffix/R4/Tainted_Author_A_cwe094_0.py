from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers.get("file_contents", None)
    if data:
        start = data.find("{") + 1
        end = len(data) - data[-1:].rfind("}")
        content = data[start:end]
        return jsonify(eval(content))
    else:
        return "No 'file_contents' found in the request."
