from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get("file_contents", "")
    start = data.find("{")
    end = data.rfind("}")
    cleaned_data = data[start : end + 1] if start != -1 and end != -1 else "{}"
    result = ast.literal_eval(cleaned_data)
    return result


if __name__ == "__main__":
    app.run(debug=True)
