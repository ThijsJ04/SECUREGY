from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex", "").strip()
    data = request.args.get("data", "").strip()

    try:
        pattern = re.compile(regex)
        if pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression"


if __name__ == "__main__":
    app.run(debug=True)
