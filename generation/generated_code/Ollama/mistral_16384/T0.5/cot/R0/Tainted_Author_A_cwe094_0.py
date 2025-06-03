from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.headers["file_contents"]
    start_index = data.find("{") if "{" in data else 0
    end_index = len(data) - 1 if "}" not in data else data.rfind("}")
    content = data[start_index : end_index + 1]
    return eval(content)
