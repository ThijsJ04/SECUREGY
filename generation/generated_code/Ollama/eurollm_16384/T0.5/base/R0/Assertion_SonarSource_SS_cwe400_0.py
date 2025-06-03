from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json.get("regex") or ".*"  # default regex is any string
    data = request.json.get("data") or ""

    if re.search(regex, data):
        return {"result": "Match found"}
    else:
        return {"result": "No match found"}
