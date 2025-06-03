from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    # Get the regex and data from the request
    search_regex = request.args.get("search_regex")
    data = request.json if "data" in request.args else request.args.get("data")

    # If no data is provided, return an error message
    if not data:
        return jsonify({"message": "No data provided"}), 400

    # Search for the regex in the data
    pattern = re.compile(search_regex)
    matches = pattern.findall(data)

    # If matches are found, return a success message with all matches
    if matches:
        return jsonify({"message": "Match found", "matches": matches}), 200
    else:
        return jsonify({"message": "No match found"}), 404
