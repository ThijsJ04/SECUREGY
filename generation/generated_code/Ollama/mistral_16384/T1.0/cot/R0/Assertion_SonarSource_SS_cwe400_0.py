from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", "")  # get regex pattern from request parameters
    data = request.args.get("data", "")  # get data to search in from request parameters

    result = re.search(
        regex, data
    )  # check if regex exists in the data using re.search()

    if result:  # if there is a match
        return "Match found"

    return "No match found"
