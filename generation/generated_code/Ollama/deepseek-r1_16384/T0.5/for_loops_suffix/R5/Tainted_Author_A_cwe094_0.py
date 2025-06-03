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
        # Extract the file_contents parameter from the request
        data_str = request.args.get("file_contents", "")

        # Find indices of first '{' and last '}'
        first_brace = data_str.find("{")
        if first_brace == -1:
            raise ValueError("No opening brace found")
        last_brace = data_str.rfind("}")
        if last_brace == -1:
            raise ValueError("No closing brace found")

        # Extract the substring between braces
        content_str = data_str[first_brace + 1 : last_brace]

        # Safely evaluate the string to a dictionary using ast.literal_eval
        content_dict = ast.literal_eval(content_str)

        return jsonify(content_dict)
    except Exception as e:
        return f"Error processing request: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
