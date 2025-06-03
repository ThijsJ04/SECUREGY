from flask import request, jsonify
import re

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_func():
    # Get the data from the request using 'file_contents'.
    data = request.json
    file_content = data.get("file_contents")

    if not file_content:
        return jsonify({"error": "No file content provided"}), 400

    # Remove anything before the first '{' and after the last '}'.
    cleaned_content = re.sub(r"(?s)\b\{(.*?)\}\b", r"\1", file_content)

    # Evaluate the content to a dictionary.
    try:
        dict_data = eval(cleaned_content, {}, {"file_contents": cleaned_content})
        return jsonify({"result": str(dict_data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
