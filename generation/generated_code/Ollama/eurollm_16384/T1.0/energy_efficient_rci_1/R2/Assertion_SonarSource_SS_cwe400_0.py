import re
from flask import request

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    try:
        regex = request.args.get("regex")
        data = request.args.get("data")
    except KeyError as e:
        return f"Missing required argument '{e}'", 400

    if not regex or not data:
        return "Required arguments are missing", 400

    search_result = re.search(regex, data)
    if search_result:
        return f"Match found at {search_result.start()}:{search_result.end() - search_result.start()}"
    else:
        return "No match found"
