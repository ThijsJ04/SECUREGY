from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from query parameters
    input_str = request.args.get("file_contents", "")

    # Extract the substring between the first '{' and last '}'
    start = input_str.find("{")
    end = input_str.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"})
    content_str = input_str[start : end + 1]

    # Evaluate the string as a dictionary
    try:
        result_dict = eval(content_str)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
