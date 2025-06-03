from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1:
        return jsonify({"error": "Invalid format"}), 400
    cleaned_data = file_contents[start_idx : end_idx + 1]
    try:
        data_dict = eval(cleaned_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(data_dict)
