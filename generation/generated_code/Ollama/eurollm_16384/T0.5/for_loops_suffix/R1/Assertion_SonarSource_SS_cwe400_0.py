import re
from flask import request, jsonify

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    search_regex = request.args.get("search_regex")
    matching_data = request.args.get("matching_data")

    if re.match(search_regex, matching_data):
        return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
