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
    pattern = re.compile(request.args.get("pattern", ""))
    data = request.args.get("data", [])

    if not pattern:
        return jsonify({"result": "No regex provided"})

    for item in data:
        if re.search(pattern, item):
            return jsonify({"result": "Match found"})

    return jsonify({"result": "No match found"})
