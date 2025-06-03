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
    # Extract regex and data from query parameters
    regex_pattern = request.args.get("regex", "")
    data_to_search = request.args.get("data", "")

    if not regex_pattern or not data_to_search:
        return jsonify({"error": "Both regex and data are required"}), 400

    try:
        # Compile the regex pattern
        pattern = re.compile(regex_pattern)
        # Search for the pattern in data
        match = pattern.search(data_to_search)
        if match:
            return jsonify({"result": "Match found"}), 200
        else:
            return jsonify({"result": "No match found"}), 200
    except re.error as e:
        # Handle invalid regex pattern
        return jsonify({"error": f"Invalid regex pattern: {str(e)}"}), 400
