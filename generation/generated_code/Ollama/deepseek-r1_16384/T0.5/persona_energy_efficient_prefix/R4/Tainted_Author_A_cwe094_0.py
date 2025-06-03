from flask import Flask, request, jsonify
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        data_str = request.form.get("file_contents", "")
        if not data_str:
            return jsonify({"error": "No file_contents provided"}), 400

        start = data_str.find("{")
        end = data_str.rfind("}")
        if start == -1 or end == -1:
            return jsonify({"error": "Invalid format, missing braces"}), 400

        content = data_str[start : end + 1]

        # Using ast.literal_eval for safe evaluation
        try:
            result = ast.literal_eval(content)
            if isinstance(result, dict):
                return jsonify(result)
            else:
                return jsonify({"error": "Result is not a dictionary"}), 400
        except ValueError as e:
            return jsonify({"error": f"Invalid literal: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
