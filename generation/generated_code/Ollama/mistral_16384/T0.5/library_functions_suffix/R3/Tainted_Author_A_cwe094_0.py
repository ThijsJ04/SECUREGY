from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    cleaned_content = (
        file_contents[1:]
        if file_contents.startswith("{")
        else file_contents[:-1]
        if file_contents.endswith("}")
        else file_contents
    )
    return json.loads(cleaned_content)
