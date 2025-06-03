from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # retrieve regex pattern from query parameters
    data = (
        request.args.get("data") or "example data"
    )  # retrieve data to search (or default value)

    if not regex:
        return (
            "No match found",
            400,
            {"message": "Please provide a valid regex pattern."},
        )

    try:
        search_result = re.search(
            regex, data, re.IGNORECASE
        )  # perform case-insensitive search
        if search_result is not None:
            return "Match found", 200
    except re.error as e:
        return "Error parsing regex", 400, {"message": "Invalid regex pattern."}

    return "No match found", 400, {}  # no match found
