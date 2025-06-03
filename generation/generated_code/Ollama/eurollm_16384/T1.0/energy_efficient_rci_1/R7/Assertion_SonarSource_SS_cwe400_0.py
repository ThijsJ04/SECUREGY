from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", default=None, type=str)
    data = request.args.get("data", default=None, type=str)

    if regex is None or data is None:
        return "Missing required arguments"

    result = re.search(regex, data)

    if result is not None:
        return f"Match found in data at position {result.start()}"
    else:
        return "No match found in data"
