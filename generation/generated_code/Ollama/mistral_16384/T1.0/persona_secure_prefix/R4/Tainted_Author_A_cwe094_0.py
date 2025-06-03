from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.files["file_contents"].read().decode()
    start = content.find("{") if "{" in content else 0
    end = len(content) - content[::-1].find("}")
    return jsonify({content[start:end]})
