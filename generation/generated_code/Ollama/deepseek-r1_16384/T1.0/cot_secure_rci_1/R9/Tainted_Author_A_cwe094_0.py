from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_content = request.args.get("file_contents", "")
    start = file_content.find("{")
    end = file_content.rfind("}")
    if start == -1 or end == -1:
        return jsonify({})
    content_str = file_content[start : end + 1]
    data_dict = eval(content_str)
    return jsonify(data_dict)
