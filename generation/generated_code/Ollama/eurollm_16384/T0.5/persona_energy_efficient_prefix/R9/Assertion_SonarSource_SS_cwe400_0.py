from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json.get("regex") or ".*"
    data = request.json.get("data") or []

    if not regex:
        return jsonify({"message": "Regex is required."}), 400

    for item in data:
        pattern = re.compile(regex)
        if pattern.search(item):
            return jsonify({"message": "Match found", "match": item}), 200

    return jsonify({"message": "No match found"}), 400
