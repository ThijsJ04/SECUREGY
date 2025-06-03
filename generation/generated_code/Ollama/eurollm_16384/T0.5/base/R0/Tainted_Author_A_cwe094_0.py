from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_contents():
    file_contents = request.args.get("file_contents")
    content = file_contents[1:-1]  # Remove '{' and '}'
    result = eval(content)
    return str(result)
