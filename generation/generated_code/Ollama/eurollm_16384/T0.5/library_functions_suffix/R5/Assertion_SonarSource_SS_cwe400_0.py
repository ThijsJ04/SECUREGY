import re
from flask import request

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    try:
        regex = re.compile(re.escape(request.args.get("regex")))
        data = request.args.get("data")
        if regex.search(data):
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        return str(e)
