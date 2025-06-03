from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    pattern = request.args.get("regex", "")
    text = request.args.get("data", "")
    if re.search(pattern, text):
        return "Match found"
    else:
        return "No match found"


if __name__ == "__main__":
    app.run(debug=True)
