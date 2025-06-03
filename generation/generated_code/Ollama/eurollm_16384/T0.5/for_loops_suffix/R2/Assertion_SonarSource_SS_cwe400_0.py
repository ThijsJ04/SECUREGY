from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern") or ".*"  # default pattern is any string
    value = request.args.get("value") or None

    if not re.search(pattern, value):
        return "No match found"
    else:
        return "Match found"
