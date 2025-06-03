from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get(
        "regex", default=None, type=str
    )  # Get regex from query string
    data = (
        request.json["data"]
        if "data" in request.json
        else request.args.get("data", default=None, type=list)
    )  # Get data from request JSON or query string
    if regex and isinstance(regex, str):
        for item in data:
            if re.search(regex, str(item)):
                return "Match found"
        return "No match found"
    else:
        return "Invalid input"
