from flask import request
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    regex = request.json.get("regex")
    data = request.json.get("data")

    match = re.search(regex, data)

    if match:
        return {"message": "Match found"}
    else:
        return {"message": "No match found"}
