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
    # Extract content from request arguments
    content = request.args.get("file_contents", "")  # or request.form.get if form data

    # Find indices of first '{' and last '}'
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        return "Invalid format", 400

    # Extract substring between braces
    content_str = content[start + 1 : end]

    try:
        # Safely evaluate the string to a dictionary using ast.literal_eval
        result = ast.literal_eval(content_str)
        if not isinstance(result, dict):
            return "Not a valid dictionary", 400
        return result
    except Exception as e:
        return f"Error during evaluation: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
