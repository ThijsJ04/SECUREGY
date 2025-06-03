from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    """
    Get regex and data from POST request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        # Get the regex pattern from the request
        pattern = re.compile(re.escape(request.form["pattern"]))

        # Get the data to search for the pattern
        data = request.form["data"]

        # Search for the pattern in the data and return the result
        if pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        return str(e)
