import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = (
        ""  # regex from query string or GET parameter (e.g., '/lookup?regex=[a-zA-Z]+')
    )
    data = (
        request.args.get("data", type=str)
        if "data" in request.args
        else request.form.get("data", type=str)
    )  # data from GET or POST parameter (e.g., query string or form data)

    if regex:
        matches = re.findall(regex, data)
        if matches:
            return "Match found"
        else:
            return "No match found"
    else:  # if no regex is provided, return help message
        return """
<form method="GET">
    {name} | {{regex}} - {{data}}
</form>
"""


if __name__ == "__main__":
    app.run(debug=True)
