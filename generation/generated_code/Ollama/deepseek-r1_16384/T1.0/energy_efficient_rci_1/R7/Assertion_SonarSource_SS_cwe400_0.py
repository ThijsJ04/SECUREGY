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
    pattern = request.args.get("regex", "").strip()
    text_data = request.args.get("data", "").strip()

    if re.search(pattern, text_data):
        return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
