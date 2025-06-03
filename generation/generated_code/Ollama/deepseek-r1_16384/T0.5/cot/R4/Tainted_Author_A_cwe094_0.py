from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return "No file_contents provided", 500
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1:
        return "Invalid content format", 500
    content_str = file_contents[start_idx + 1 : end_idx]
    try:
        result_dict = ast.literal_eval(content_str)
        return str(result_dict), 200
    except Exception as e:
        return f"Error parsing content: {str(e)}", 500
