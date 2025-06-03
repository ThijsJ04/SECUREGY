from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    raw_data = request.files["file_contents"].read().decode("utf-8")
    data = json.loads(raw_data[raw_data.find("{") :]) if "{" in raw_data else {}
    return jsonify(data)
