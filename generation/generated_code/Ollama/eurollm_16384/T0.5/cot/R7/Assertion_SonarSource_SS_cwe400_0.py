from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    regex = request.args.get("regex")
    data = request.json or request.form
    match = (
        bool(re.search(regex, str(data)))
        if isinstance(data, str)
        else any(re.search(regex, x) for x in data)
    )
    return "Match found" if match else "No match found"
