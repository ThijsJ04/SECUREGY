from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return jsonify({})

    content_str = file_contents[start : end + 1]

    try:
        result = json.loads(content_str)
    except json.JSONDecodeError:
        return jsonify({})

    return jsonify(result)
