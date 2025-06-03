from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", default=None, type=str)
    data = request.args.get("data", default=None, type=str)

    if regex is None or data is None:
        return "Error: Missing required arguments"

    match = re.search(regex, data)

    if match:
        return "Match found"
    else:
        return "No match found"
