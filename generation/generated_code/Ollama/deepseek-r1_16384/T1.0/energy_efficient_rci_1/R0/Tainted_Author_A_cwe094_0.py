from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.form.get("file_contents", "")
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    cleaned_content = file_contents[start_index : end_index + 1]
    result_dict = json.loads(cleaned_content)
    return jsonify(result_dict)
