import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Perform a text search using regular expressions and return the result.

    :param regex: The regular expression pattern to be searched.
    :param data: The input data to be searched.
    :return: "Match found" if the match is found, otherwise "No match found".
    """
    regex = request.args.get("regex")  # Get regex from query parameters
    data = request.args.get("data")  # Get data from query parameters
    if not regex or not data:
        return "Error: Missing required parameters", 400

    match = re.search(regex, data)  # Perform the search using regular expressions
    if match:
        return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
