from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)
    if not file_contents:
        return jsonify({"error": "No file contents provided."}), 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents.strip("{}").strip()

    try:
        result = eval(cleaned_content)
        if isinstance(result, dict):
            return jsonify(result)
        else:
            return jsonify(
                {"error": "The provided content is not a valid dictionary."}
            ), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
