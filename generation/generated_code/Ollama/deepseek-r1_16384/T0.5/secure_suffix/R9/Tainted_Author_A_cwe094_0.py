from flask import Flask, request
import ast  # Using safer eval with AST

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents") or request.form.get(
        "file_contents"
    )

    if not file_contents:
        return {}

    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")

    if start_index == -1 or end_index == -1 or start_index > end_index:
        return {}

    content_str = file_contents[start_index : end_index + 1]

    try:
        # Use ast.literal_eval for safer evaluation
        content_dict = ast.literal_eval(content_str)
        if isinstance(content_dict, dict):
            return content_dict
        else:
            return {}
    except (ValueError, SyntaxError):
        return {}


if __name__ == "__main__":
    app.run(debug=True)
