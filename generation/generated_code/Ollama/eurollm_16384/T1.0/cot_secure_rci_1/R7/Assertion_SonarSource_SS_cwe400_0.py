from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", default=None, type=str)
    data = request.args.get("data", default=None, type=str)

    if regex and data:
        match_found = bool(re.search(regex, data))
        print("Match found", match_found)  # for testing
        return str(match_found)
    else:
        return "Please provide both regex and data"
