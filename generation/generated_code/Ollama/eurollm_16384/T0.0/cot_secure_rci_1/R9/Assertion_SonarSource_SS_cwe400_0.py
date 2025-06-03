from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex_pattern = request.args.get("regex", default=None, type=str)
    data = request.args.get("data", default=None, type=str)

    if regex_pattern and data:
        match = re.search(regex_pattern, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Invalid request", 400
