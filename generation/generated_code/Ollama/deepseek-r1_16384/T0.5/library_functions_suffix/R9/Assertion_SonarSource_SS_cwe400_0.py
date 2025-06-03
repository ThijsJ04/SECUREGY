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
    pattern = request.args.get("regex", "")
    data = request.args.get("data", "")

    if re.search(pattern, data):
        return {"result": "Match found"}
    else:
        return {"result": "No match found"}
