from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", "")
    start = data.find("{")
    end = data.rfind("}")
    if start != -1 and end != -1:
        content = data[start + 1 : end]
        try:
            result = eval(content)
        except:
            result = {}
    else:
        result = {}
    return json.dumps(result)
