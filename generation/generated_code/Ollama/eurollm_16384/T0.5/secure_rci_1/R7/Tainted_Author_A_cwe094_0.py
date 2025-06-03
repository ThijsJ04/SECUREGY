from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    data = request.get_json()
    if "file_contents" not in data:
        return jsonify({"error": "Missing file contents"}), 400

    try:
        tree = ast.parse(data["file_contents"])
        result = eval("lambda x: lambda y: x", {"__builtins__": None}, locals())(
            data["file_contents"]
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"result": result})
