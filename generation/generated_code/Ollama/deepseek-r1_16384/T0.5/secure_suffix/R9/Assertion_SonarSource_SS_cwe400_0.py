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
    regex = request.values.get("regex", "", "utf-8")
    data = request.values.get("data", "", "utf-8")

    if not regex or not data:
        return {"error": "Regex or data is missing"}, 400

    if re.search(regex, data, flags=re.IGNORECASE):
        return {"result": "Match found"}
    else:
        return {"result": "No match found"}
