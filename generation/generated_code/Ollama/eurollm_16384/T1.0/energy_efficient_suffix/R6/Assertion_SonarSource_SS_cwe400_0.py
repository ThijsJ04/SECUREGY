import re
from flask import request

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    # Extract regex and data from the request
    regex = request.form.get("regex") or ""
    data = request.form.get("data") or ""

    # Check if regex is empty
    if not regex:
        return "No match found"

    # Use re.search to find the regex in the data
    match = re.search(regex, data)

    # Return "Match found" or "No match found" based on whether a match was found
    if match:
        return "Match found"
    else:
        return "No match found"
