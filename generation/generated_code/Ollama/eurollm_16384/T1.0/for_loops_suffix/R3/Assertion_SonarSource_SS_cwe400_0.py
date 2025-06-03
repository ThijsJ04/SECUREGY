from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".
    """
    try:
        regex = request.args.get("regex")
        data = request.args.get("data")

        if regex and data:
            result = re.search(regex, data)
            if result:
                return f"Match found!"
            else:
                return "No match found."
    except KeyError:
        pass  # handle missing arguments

    return "Missing required arguments", 400
