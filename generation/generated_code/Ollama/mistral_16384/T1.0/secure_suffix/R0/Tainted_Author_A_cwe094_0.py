from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    start_index = file_contents.find("{") + 1 if "{" in file_contents else 0
    end_index = len(file_contents) - 1 if file_contents[-1] == "}" else None

    if not end_index:
        return jsonify({"error": "Invalid JSON structure."}), 400

    content = file_contents[start_index:end_index]
    try:
        result = eval(content)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(result)
