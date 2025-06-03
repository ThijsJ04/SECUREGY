import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.get_json()  # Assuming JSON data is sent in the POST request
    regex = request.form.get("regex") if "regex" in request.form else None

    if regex:
        for item in data["items"]:
            if re.search(regex, str(item)):
                return f"Match found: {item}"
    else:
        return "No match found."
