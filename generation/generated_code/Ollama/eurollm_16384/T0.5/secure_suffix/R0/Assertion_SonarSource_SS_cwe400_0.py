from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get(
        "regex"
    )  # Get the regex pattern from query string or form data
    data = (
        request.json if "data" in request.args else request.form
    )  # Get the data to search for the regex pattern

    match_found = False
    for item in data:
        if re.search(regex, str(item)):
            match_found = True
            print("Match found")
            break

    if not match_found:
        print("No match found")
        return jsonify({"result": "No match found"})  # Return the result as JSON

    print("Match found")
    return jsonify({"result": "Match found"})  # Return the result as JSON
