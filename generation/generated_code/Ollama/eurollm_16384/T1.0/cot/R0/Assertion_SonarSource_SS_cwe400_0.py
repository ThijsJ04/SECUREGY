from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    if not regex or not data:
        return "Please provide both regex and data for lookup."

    match_found = re.search(regex, data) is not None
    result = {"match": match_found}

    return jsonify(result)
