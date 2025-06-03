import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # Get regex from query string
    data = request.args.get("data")  # Get data to search in

    if not regex or not data:
        return jsonify({"message": "Invalid input"}), 400

    match = re.search(regex, data)
    if match:
        return jsonify({"message": "Match found", "matched_data": match.group()})
    else:
        return jsonify({"message": "No match found"}), 200
