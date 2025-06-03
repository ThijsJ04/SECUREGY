from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input data from the request
    data = request.args.get("file_contents", "")

    # Extract content between the first '{' and last '}'
    start = data.find("{")
    end = data.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"})

    cleaned_data = data[start : end + 1]

    # Evaluate the cleaned string to a dictionary
    try:
        result = eval(cleaned_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
