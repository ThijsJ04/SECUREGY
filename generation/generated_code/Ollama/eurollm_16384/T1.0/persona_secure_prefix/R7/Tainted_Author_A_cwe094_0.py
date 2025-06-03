from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def eval_func():
    file_contents = request.args.get("file_contents", default="", type=str)
    content = file_contents[
        1:-1
    ]  # Remove everything before the first '{' and after the last '}'

    try:
        result = json.loads(content)
        return str(result)
    except ValueError as e:
        return str(e)
