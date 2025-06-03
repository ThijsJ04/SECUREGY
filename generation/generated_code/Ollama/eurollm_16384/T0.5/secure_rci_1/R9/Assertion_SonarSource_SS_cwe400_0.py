from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", default="", type=str)
    data = request.args.get("data", default="example data", type=str)

    if regex and data:
        match = re.search(regex, data)
        if match:
            return f"Match found in '{data}' at position {match.start()} with length {len(match.group())} characters."
        else:
            return "No match found in '{}'".format(data)
    else:
        return "Error: Missing required arguments. Please provide regex and data."
