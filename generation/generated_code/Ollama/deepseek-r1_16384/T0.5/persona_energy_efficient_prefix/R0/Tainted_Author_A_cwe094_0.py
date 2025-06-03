from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input data
    data = request.get_json()

    # Extract the file contents string
    file_contents = data.get("file_contents", "")

    # Find the indices of the first '{' and last '}'
    start = file_contents.find("{")
    end = file_contents.rfind("}")

    if start == -1 or end == -1:
        return {"error": "Invalid format"}, 400

    # Slice the string to get only the content between braces
    content_to_eval = file_contents[start : end + 1]

    try:
        # Evaluate the string as a dictionary
        result = eval(content_to_eval)
        return result
    except Exception as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True)
