from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    data = request.args.get(
        "data", default="example text"
    )  # get data from query string or default value if not provided
    regex = request.args.get(
        "regex", default=r"\b\w+\b"
    )  # get regex pattern from query string or default value if not provided

    try:
        matches = re.findall(regex, data)
        print(f"Match found: {' '.join(matches)}")
    except AttributeError:
        print("No match found")

    return "Search result:"
