from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = re.compile(
        request.args.get("pattern")
    )  # Get the pattern from request arguments
    data = request.args.get("data")  # Get the data from request arguments
    match = regex.search(
        data
    )  # Search for a match in the data using the provided pattern
    if match:
        return "Match found"
    else:
        return "No match found"
