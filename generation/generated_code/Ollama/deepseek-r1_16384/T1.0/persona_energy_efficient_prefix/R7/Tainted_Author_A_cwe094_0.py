from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data_str = request.form.get("file_contents")
    start = data_str.find("{")
    end = data_str.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid content format"}), 400
    cleaned_data = data_str[start : end + 1]
    try:
        data_dict = json.loads(cleaned_data)
        return jsonify(data_dict)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse JSON"}), 400


if __name__ == "__main__":
    app.run(debug=True)
