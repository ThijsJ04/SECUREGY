from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # get regex from query string
    data = request.args.get("data")  # get data to search in

    if regex:
        match = re.search(r"{}".format(regex), data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Please provide a regex pattern to search."
