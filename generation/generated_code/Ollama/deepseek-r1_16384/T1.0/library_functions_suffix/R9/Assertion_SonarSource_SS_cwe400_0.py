from flask import request
from flask import Flask
import re
from flask.json import jsonify

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Extract regex pattern and data from request parameters
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")

    # Validate inputs
    if not regex or not data:
        return jsonify({"error": "Regex or data is missing"}), 400

    try:
        # Search for the pattern in data
        match = re.search(regex, data)
        if match:
            return jsonify("Match found")
        else:
            return jsonify("No match found")

    except re.error as e:
        return jsonify({"error": f"Invalid regex pattern: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
