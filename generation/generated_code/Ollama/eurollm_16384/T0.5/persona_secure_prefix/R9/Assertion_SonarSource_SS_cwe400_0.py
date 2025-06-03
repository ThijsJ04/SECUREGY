from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    try:
        # Get regex from request parameters
        pattern = request.args.get("pattern")

        # Get data from request body (or query string)
        data = request.args.get("data") or request.args.get("query")

        # Search for regex in data
        match = re.search(pattern, data)
        if match:
            return f"Match found"
        else:
            return "No match found"
    except Exception as e:
        print("Error:", str(e))
        return "An error occurred."
