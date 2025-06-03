from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex_pattern = request.args.get("regex", "")
    data_string = request.args.get("data", "")

    if re.search(regex_pattern, data_string):
        return "Match found"
    else:
        return "No match found"


if __name__ == "__main__":
    app.run(debug=True)
