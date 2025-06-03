from flask import Flask, request, jsonify
import json
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    data = request.get_json()
    file_contents = data.get("file_contents")

    if file_contents is None:
        return jsonify({"error": "No file content provided"}), 400

    content = file_contents
    for k in ["{", "}"]:
        content = re.sub(k, "", content)

    try:
        json_dict = json.loads(content)
        return jsonify({"dictionary": json_dict})
    except ValueError as e:
        return jsonify({"error": str(e)}), 500
