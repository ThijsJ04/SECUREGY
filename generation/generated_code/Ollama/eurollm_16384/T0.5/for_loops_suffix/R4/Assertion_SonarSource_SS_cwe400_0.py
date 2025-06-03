from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    # Get regex and data from request
    pattern = request.json.get("pattern")
    data = request.json.get("data")

    # Check if both pattern and data are provided
    if not pattern or not data:
        return jsonify({"message": "Both pattern and data must be provided"}), 400

    # Search for regex in data
    try:
        match = re.search(pattern, data)
        if match:
            return jsonify({"result": "Match found"})
        else:
            return jsonify({"result": "No match found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
