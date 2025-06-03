from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET", "POST"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    if request.method == "POST":
        try:
            data = request.get_json()
            regex = data["regex"]
            text_to_search = data["data"]
        except KeyError as e:
            return "Missing parameters", 400
        except ValueError:
            return "Invalid JSON", 400
    else:
        regex = request.args.get("regex", "")
        text_to_search = request.args.get("data", "")

    if not regex or not text_to_search:
        return "No match found"

    try:
        if re.search(regex, text_to_search):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regex", 400
