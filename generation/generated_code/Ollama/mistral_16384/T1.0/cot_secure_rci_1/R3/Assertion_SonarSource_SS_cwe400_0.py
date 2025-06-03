from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", None)
    data = request.args.get("data", None)

    if regex and data:
        match = re.search(regex, data)
        return "Match found" if match else "No match found"
    return "Please provide both regex and data in the query string."
