from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", default=None, type=str)
    if file_contents is None or not file_contents:
        return jsonify({"error": "No valid JSON provided."}), 400

    # Remove anything before the first '{' and after the last '}'
    cleaned = file_contents.strip("{}").replace("\n", "")

    try:
        return jsonify(eval(cleaned))
    except Exception as e:
        return jsonify({"error": str(e)}), 400
