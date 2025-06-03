from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Extract file_contents parameter from request
    data = request.args.get("file_contents", "")

    # Find the indices of the first '{' and last '}'
    start = data.find("{")
    end = data.rfind("}")

    if start == -1 or end == -1:
        return jsonify({})  # Return empty dict if braces not found

    # Slice the string to get content between braces
    content = data[start + 1 : end]

    # Evaluate the content as a dictionary and return it
    try:
        result = eval(content)
        return jsonify(result)
    except:
        return jsonify({})  # Return empty dict if evaluation fails
