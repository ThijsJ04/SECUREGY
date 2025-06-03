import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    pattern = request.args.get("pattern")  # get regex pattern from URL query params
    data = request.json["data"]  # get JSON data from request body

    matches = re.findall(
        pattern, str(data)
    )  # find matches of regex in data using `re.findall()`

    if matches:
        return jsonify(
            {"result": "Match found", "matches": [match for match in matches]}
        )
    else:
        return jsonify({"result": "No match found"})
