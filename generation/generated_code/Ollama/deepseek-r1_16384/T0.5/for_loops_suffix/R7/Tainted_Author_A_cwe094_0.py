from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    content_str = file_contents[start_index : end_index + 1]
    return eval(content_str)
