from flask import Flask, request
import ast  # Using ast.literal_eval for safer evaluation

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from request parameters or form data
    content = request.args.get("file_contents") or request.form.get("file_contents")

    if not content:
        return {}  # Return empty dict if no content provided

    # Find indices of first '{' and last '}'
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        return {}  # Invalid format, return empty dict

    # Extract the substring between braces
    content_str = content[start + 1 : end]

    try:
        # Safely evaluate the string to a dictionary using ast.literal_eval
        content_dict = ast.literal_eval(content_str)
        if isinstance(content_dict, dict):
            return content_dict
        else:
            return {}  # Return empty dict if not a dictionary
    except (ValueError, SyntaxError):
        return {}  # Return empty dict on evaluation errors


if __name__ == "__main__":
    app.run(debug=True)
