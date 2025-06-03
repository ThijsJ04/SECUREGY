from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    pattern = request.args.get("pattern")
    data = request.args.get("data")

    if re.search(pattern, data):
        return f"Match found"
    else:
        return f"No match found"
