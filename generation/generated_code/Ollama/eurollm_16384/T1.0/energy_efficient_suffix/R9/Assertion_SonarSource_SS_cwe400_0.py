import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex_str = request.args.get("regex")
    data_str = request.args.get("data")

    # Remove any leading or trailing whitespace from the regex string
    if regex_str:
        regex_str = regex_str.strip()
    else:
        abort(400)  # 400 Bad Request if no regex provided

    if not data_str:
        abort(400)  # 400 Bad Request if no data provided

    try:
        regex = re.compile(regex_str, re.IGNORECASE)
        matches = regex.findall(data_str)
        if matches:
            return "Match found"
        else:
            return "No match found"
    except Exception as e:
        abort(500)  # 500 Internal Server Error if any error occurs during regex search


if __name__ == "__main__":
    app.run()
