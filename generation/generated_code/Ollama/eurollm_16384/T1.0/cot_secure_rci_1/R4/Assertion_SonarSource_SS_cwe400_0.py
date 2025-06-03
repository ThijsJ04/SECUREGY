import re
from flask import request

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex_pattern = request.args.get(
        "regex"
    )  # Get regex pattern from the URL query string (e.g., '/lookup?regex=a*b+c*d')
    data = request.args.get(
        "data", default="Hello, World!"
    )  # Get data to search for from the URL query string or by default as a string literal
    words = re.split(
        " |\n|;|\t", data
    )  # Split data into words using whitespace, newlines, semicolons, and tabs

    for word in words:
        if regex_pattern == r"\b" + re.escape(
            word
        ):  # Check if the current word matches the regex pattern
            return "Match found"

    return "No match found"
