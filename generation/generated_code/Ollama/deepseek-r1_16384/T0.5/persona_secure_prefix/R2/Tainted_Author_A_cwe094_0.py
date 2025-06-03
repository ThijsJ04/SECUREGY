from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return jsonify({"error": "No content provided"}), 400

    # Extract the substring between first '{' and last '}'
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    if start_index == -1 or end_index == -1:
        return jsonify({"error": "Invalid content format"}), 400

    cleaned_content = file_contents[start_index : end_index + 1]

    try:
        # Evaluate the cleaned string as a dictionary
        result_dict = eval(cleaned_content)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
