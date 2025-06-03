from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json.get("regex") or ""
    data = request.json.get("data") or []

    for item in data:
        if re.search(regex, str(item)):
            return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
