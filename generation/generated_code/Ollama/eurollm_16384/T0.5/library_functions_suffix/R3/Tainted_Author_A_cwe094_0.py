from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.get_json()
    content = file_contents["content"]

    # Remove anything before the first '{' and after the last '}'
    content = content[
        1:-1
    ]  # Assuming the JSON is well-formed with no extra whitespace or comments

    return json.dumps(eval(content))
