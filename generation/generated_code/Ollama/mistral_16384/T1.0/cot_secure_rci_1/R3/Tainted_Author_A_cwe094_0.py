from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)
    if file_contents:
        start_index = file_contents.find("{") + 1
        end_index = len(file_contents) - file_contents[-1:].rfind("}")
        content = file_contents[start_index:end_index]
        return json.loads(content)
    else:
        return {"error": "No data found in the request"}
