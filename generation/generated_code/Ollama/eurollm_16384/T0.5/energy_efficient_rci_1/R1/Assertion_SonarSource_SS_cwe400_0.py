from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get(
        "regex", default="^[a-zA-Z]+"
    )  # Default regex if not provided in query string
    data = request.json["data"]  # Assuming JSON data is sent via the request body

    matches = [match for match in re.finditer(regex, str(data))]
    if matches:
        return jsonify({"result": "Match found"})
    else:
        return jsonify({"result": "No match found"})
