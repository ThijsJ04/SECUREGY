from flask import Flask, request
import ast  # Using ast.literal_eval for safe evaluation

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    # Extract content between first '{' and last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return {}  # Return empty dict if no braces found
    content = file_contents[start + 1 : end]
    try:
        # Safely evaluate the content as a dictionary
        return ast.literal_eval(content)
    except (ValueError, SyntaxError):
        return {}
