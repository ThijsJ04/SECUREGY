import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_data():
    data = request.get_json()
    return json.dumps(
        data, indent=4
    )  # or simply return the parsed JSON as-is without any further modification
