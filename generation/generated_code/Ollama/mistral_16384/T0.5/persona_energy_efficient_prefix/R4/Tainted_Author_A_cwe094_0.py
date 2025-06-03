from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.files["file_contents"].read().decode("utf-8")
    start_index = data.find("{") if "{" in data else 0
    end_index = len(data) - 1 if "}" not in data else data.rfind("}")
    content = data[start_index : end_index + 1]
    return jsonify(eval(content))
