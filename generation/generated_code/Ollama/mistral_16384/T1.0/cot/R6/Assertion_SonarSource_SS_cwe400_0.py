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

    # Extract regex and data from the request
    regex = re.compile(request.args.get("regex"))
    data = request.args.get("data")

    # Check if regex matches data, return appropriate message
    if regex.search(data):
        return "Match found"
    else:
        return "No match found"
