from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    pattern = request.args.get(
        "pattern",
        default="^([a-zA-Z0-9]+)$",
    )
    value = request.args.get("value", "")

    if re.match(pattern, value):
        return "Match found"
    else:
        return "No match found"
