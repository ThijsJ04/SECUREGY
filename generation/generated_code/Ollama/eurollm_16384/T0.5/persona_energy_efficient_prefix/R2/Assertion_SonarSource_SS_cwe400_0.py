from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern") or ".*"
    value = request.args.get("value") or ""

    if re.search(pattern, value):
        return f"Match found"
    else:
        return f"No match found"
