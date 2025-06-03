from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")
    match_found = re.search(regex, data) is not None
    return f"Match found if regex matches in data else No match found."
