from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents")
    if data:
        start_index = data.find("{") + 1
        end_index = data.rfind("}")
        content = data[start_index:end_index]
        return jsonify(eval(content))
