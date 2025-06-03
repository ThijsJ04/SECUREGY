from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    try:
        regex = request.args.get("regex")
        data = request.args.get("data")
    except ValueError:
        return "Missing regex or data in URL query parameters"

    if not re.match(regex, data):
        return "No match found"
    else:
        return "Match found"
