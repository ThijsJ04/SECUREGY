from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")
    # Extract the content between the first { and last }
    start = file_contents.find("{")
    end = file_contents.rfind("}")
    if start == -1 or end == -1:
        return "Invalid format. Content must be enclosed in {}"
    content_str = file_contents[start + 1 : end]
    try:
        # Evaluate the extracted string as a dictionary
        content_dict = ast.literal_eval(content_str)
        return str(content_dict)
    except Exception as e:
        return f"Error evaluating content: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
