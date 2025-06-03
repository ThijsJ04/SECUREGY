from flask import request
from flask import Flask
import re
from flask import jsonify

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")

    if not regex or not data:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        if re.search(regex, data):
            return jsonify({"result": "Match found"}), 200
        else:
            return jsonify({"result": "No match found"}), 200
    except re.error as e:
        print(f"Regex error: {e}")
        return jsonify({"error": "Invalid regex"}), 400
