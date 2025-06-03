from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # Get the regex from the query string
    data = request.args.get("data")  # Get the data from the query string

    if regex and data:
        match = re.search(regex, data)
        if match:
            return f"Match found in '{data}' at position {match.start()} with length {len(match.group())}."
        else:
            return "No match found in '{}'".format(data)
    else:
        return "Error: Both regex and data are required."
