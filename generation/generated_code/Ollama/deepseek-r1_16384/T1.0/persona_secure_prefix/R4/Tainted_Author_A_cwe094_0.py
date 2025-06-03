from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", "")
    start_index = data.find("{")
    end_index = data.rfind("}")
    content_to_eval = data[start_index + 1 : end_index]
    result = eval(content_to_eval)
    return json.dumps(result)
