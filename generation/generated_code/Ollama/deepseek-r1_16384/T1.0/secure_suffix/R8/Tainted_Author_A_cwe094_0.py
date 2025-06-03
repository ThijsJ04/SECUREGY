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
    # Get data from the request
    file_contents = ""
    if "file_contents" in request.form:
        file_contents = request.form["file_contents"]
    elif "file_contents" in request.json:
        file_contents = request.json.get("file_contents", "")

    # Extract content between first '{' and last '}'
    start_idx = file_contents.find("{")
    end_idx = file_contents.rfind("}")
    if start_idx == -1 or end_idx == -1 or start_idx > end_idx:
        return "Invalid format", 400
    content_str = file_contents[start_idx + 1 : end_idx]

    # Evaluate the string to a dictionary safely
    try:
        content_dict = ast.literal_eval(content_str)
        if not isinstance(content_dict, dict):
            return "Not a valid dictionary", 400
    except (ValueError, SyntaxError) as e:
        return f"Invalid syntax: {str(e)}", 400

    # Return the dictionary as JSON response
    from flask import jsonify

    return jsonify(content_dict)


if __name__ == "__main__":
    app.run(debug=True)
