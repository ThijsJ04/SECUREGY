from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.get_json().get("file_contents", "")
    start = file_contents.find("{")
    if start == -1:
        return jsonify({"error": "No opening brace found"})
    end = file_contents.rfind("}")
    if end == -1:
        return jsonify({"error": "No closing brace found"})
    content_str = file_contents[start + 1 : end].strip()
    try:
        data_dict = eval(content_str)
    except Exception as e:
        return jsonify({"error": str(e)})
    return jsonify(data_dict)
