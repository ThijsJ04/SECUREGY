from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """

    # extract regex from the request
    regex_pattern = re.compile(request.args.get("regex"))
    # extract data from the request
    data = request.args.get("data")

    if regex_pattern.search(data):
        return "Match found"
    else:
        return "No match found"
