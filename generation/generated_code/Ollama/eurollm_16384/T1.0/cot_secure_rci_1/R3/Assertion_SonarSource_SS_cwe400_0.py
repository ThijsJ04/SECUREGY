from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    # Convert regex to a pattern object
    pattern = re.compile(regex)

    if pattern.search(data):
        return "Match found"
    else:
        return "No match found"
