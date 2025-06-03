from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Extract parameters from request
    regex_pattern = request.args.get("regex", "")
    data_to_search = request.args.get("data", "")

    if not regex_pattern or not data_to_search:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        pattern = re.compile(regex_pattern)
        match = pattern.search(data_to_search)
        if match:
            return jsonify({"result": "Match found"}), 200
        else:
            return jsonify({"result": "No match found"}), 404
    except re.error as e:
        return jsonify({"error": f"Invalid regex pattern: {str(e)}"}), 400
