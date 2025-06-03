from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    file_contents = request.form["file_contents"]  # get file contents from form data
    start_tag = "{"
    end_tag = "}"

    for char in file_contents:
        if char == start_tag:
            continue
        elif char == end_tag:
            break
        content_dict = eval(
            file_contents[
                file_contents.find(start_tag) + 1 : file_contents.rfind(end_tag)
            ]
        )  # start from the first non-opening brace and stop at the last closing brace
        return json.dumps(
            content_dict, indent=4
        )  # format response as JSON with indentation
