from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers["file_contents"]
    start_index = data.find("{") if "{".lower() in data else 0
    end_index = data.rfind("}")
    content = data[start_index : end_index + 1]
    return jsonify(eval(content))
