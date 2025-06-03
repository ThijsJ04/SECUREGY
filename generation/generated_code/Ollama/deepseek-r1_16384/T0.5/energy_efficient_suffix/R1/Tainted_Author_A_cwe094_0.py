from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return jsonify({"error": "No file_contents provided"}), 400
    start_index = file_contents.find("{")
    if start_index == -1:
        return jsonify({"error": "No opening brace found"}), 400
    end_index = file_contents.rfind("}")
    if end_index == -1 or end_index < start_index:
        return jsonify({"error": "No closing brace found"}), 400
    content_to_eval = file_contents[start_index : end_index + 1]
    try:
        result_dict = eval(content_to_eval)
        if not isinstance(result_dict, dict):
            raise ValueError("Evaluated content is not a dictionary")
        return jsonify(result_dict)
    except Exception as e:
        app.logger.error(f"Error processing contents: {e}")
        return jsonify({"error": str(e)}), 500
