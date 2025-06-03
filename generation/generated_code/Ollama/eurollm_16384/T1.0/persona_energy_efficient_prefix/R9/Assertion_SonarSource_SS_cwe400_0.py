import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    try:
        # Get the regex and data from the request
        search_regex = re.search(
            r"pattern", request.args.get("data"), re.IGNORECASE
        ).group()
    except AttributeError:
        return "No valid arguments provided"

    # Search for the regex in the data
    if search_regex:
        return f"Match found at index {search_regex}"
    else:
        return f"No match found in the data"
