from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_file():
    """
    Evaluate the content of a file as a Python expression and return the result.
    """
    data = request.get_json()
    if not "file_contents" in data:
        return jsonify({"error": "Missing file contents."}), 400

    # Remove anything before the first '{' and after the last '}' from the file contents
    content = data["file_contents"].strip("{}")

    # Evaluate the content as a Python expression
    try:
        result = eval(content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"result": result})
