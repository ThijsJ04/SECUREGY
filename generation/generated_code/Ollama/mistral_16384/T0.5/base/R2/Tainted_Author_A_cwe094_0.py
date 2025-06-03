from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)
    if not file_contents:
        return jsonify({"error": "No file contents provided."}), 400

    start = file_contents.find("{") + 1
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid JSON format."}), 400

    cleaned_content = file_contents[start:end]
    try:
        result = eval(cleaned_content)
    except Exception as e:
        return jsonify({"error": f"Error while parsing JSON: {str(e)}"}), 400

    return jsonify(result)
