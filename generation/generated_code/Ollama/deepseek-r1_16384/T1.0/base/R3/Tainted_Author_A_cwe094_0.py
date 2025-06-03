from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return "Bad request", 400
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1:
        return "Bad request", 400
    content_to_eval = file_contents[start_idx + 1 : end_idx]
    try:
        data_dict = eval(content_to_eval)
        if not isinstance(data_dict, dict):
            raise ValueError("Content is not a dictionary.")
    except (NameError, SyntaxError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(data_dict)
