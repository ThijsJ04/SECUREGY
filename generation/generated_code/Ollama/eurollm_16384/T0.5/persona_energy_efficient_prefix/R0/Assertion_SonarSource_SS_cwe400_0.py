from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    if regex and data:
        match_found = re.search(regex, data) is not None
        print("Match found" if match_found else "No match found")
        return f"Match found" if match_found else "No match found"
    else:
        return "Please provide regex and data."
