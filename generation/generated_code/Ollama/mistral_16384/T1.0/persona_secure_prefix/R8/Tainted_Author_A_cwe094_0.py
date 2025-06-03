from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    raw_data = request.files["file_contents"].read().decode("utf-8")
    cleaned_data = raw_data[raw_data.index("{") :].strip()
    return jsonify(json.loads(cleaned_data))
