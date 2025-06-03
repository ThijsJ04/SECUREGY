from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.form.get("file_contents", "")
    start_index = data.find("{")
    end_index = data.rfind("}")
    content_str = (
        data[start_index : end_index + 1]
        if start_index != -1 and end_index != -1
        else ""
    )
    try:
        result_dict = ast.literal_eval(content_str)
        return jsonify(result_dict)
    except ValueError as e:
        return f"Error parsing dictionary: {e}", 400


if __name__ == "__main__":
    app.run(debug=True)
