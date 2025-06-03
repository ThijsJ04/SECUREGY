from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_pattern = request.args.get("regex")
    data = request.args.get("data")

    # Validate regex pattern
    if not re.match(
        r"\A[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\Z", regex_pattern
    ):
        return jsonify({"error": "Invalid regex pattern"}), 400

    # Validate data
    try:
        data = data.strip()
    except AttributeError:
        return jsonify({"error": "Data is not a string"}), 400

    if not re.search(regex_pattern, data):
        return jsonify({"result": "No match found"})
    else:
        return jsonify({"result": "Match found"})
