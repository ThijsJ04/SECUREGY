from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.args.get("file_contents", default=None)
    if content is not None:
        start_index = content.find("{") + 1
        end_index = content.rfind("}")
        if start_index != -1 and end_index != -1:
            return {eval(content[start_index:end_index])}
    return {}
