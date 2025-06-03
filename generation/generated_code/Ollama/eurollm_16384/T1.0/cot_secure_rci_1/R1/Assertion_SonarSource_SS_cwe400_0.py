from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    pattern = (
        re.compile(re.escape(request.args["pattern"]))
        if "pattern" in request.args
        else None
    )
    data = request.data

    if pattern and pattern.search(data):
        return "Match found"
    else:
        return "No match found"
