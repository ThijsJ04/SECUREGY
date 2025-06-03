from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers["file_contents"]
    start = data.find("{") if "{" in data else 0
    end = len(data) - data[-1:].rfind("}") if "}" in data[-1:] else len(data)
    content = data[start:end]
    return jsonify(eval(content))
