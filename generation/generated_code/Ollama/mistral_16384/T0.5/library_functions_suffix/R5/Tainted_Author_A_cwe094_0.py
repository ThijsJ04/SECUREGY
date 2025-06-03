from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.args.get("file_contents", default=None) or request.data
    if content:
        start_index = content.find("{") + 1
        end_index = content.rfind("}")
        if start_index > 0 and end_index > start_index:
            return {json.loads(content[start_index:end_index])}
    return {}
