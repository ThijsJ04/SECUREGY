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
    if not file_contents:
        return "No file_contents provided", 400

    try:
        # Find the indices of the first and last curly braces
        start = file_contents.find("{")
        end = file_contents.rfind("}")

        if start == -1 or end == -1:
            return "Invalid format, missing braces", 400

        content = file_contents[start + 1 : end]

        # Safely evaluate the content as a dictionary
        result = ast.literal_eval(content)
        return str(result), 200
    except Exception as e:
        return f"Error processing contents: {str(e)}", 400


if __name__ == "__main__":
    app.run(debug=True)
