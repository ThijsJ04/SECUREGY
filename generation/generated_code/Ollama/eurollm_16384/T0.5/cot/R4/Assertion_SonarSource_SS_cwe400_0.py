from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex_pattern = request.args.get("regex")
    data = request.args.get("data")

    # Parse regex pattern
    regex = re.compile(regex_pattern)

    # Search for regex in data
    if regex.search(data):
        return "Match found"
    else:
        return "No match found"
