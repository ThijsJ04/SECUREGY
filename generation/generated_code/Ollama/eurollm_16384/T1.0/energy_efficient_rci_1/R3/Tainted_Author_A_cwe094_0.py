from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_json():
    data = request.get_json()  # get the data from the request using 'file_contents'
    key = data.pop(
        "key", None
    )  # remove anything before the first '{' and after the last '}'
    return json.dumps(eval("{{ %s }}" % key), indent=4, sort_keys=True)
