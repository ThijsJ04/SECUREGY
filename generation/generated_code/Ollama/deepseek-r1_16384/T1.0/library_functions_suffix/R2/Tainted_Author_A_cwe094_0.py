from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    if start_index == -1 or end_index == -1:
        return {}

    content_to_eval = file_contents[start_index : end_index + 1]

    try:
        data_dict = json.loads(content_to_eval)
    except json.JSONDecodeError:
        return {}

    return data_dict
