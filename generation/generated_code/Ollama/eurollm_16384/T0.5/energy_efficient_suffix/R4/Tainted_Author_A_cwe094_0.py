from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    content = file_contents[
        1:-1
    ]  # remove everything before the first '{' and after the last '}'
    return json.dumps(eval(content))
