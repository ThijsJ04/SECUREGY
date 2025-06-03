from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Extract the file_contents parameter from the request
    data = request.args.get("file_contents", "")

    # Remove everything before the first '{' and after the last '}'
    cleaned_data = data.split("{", 1)[-1].rsplit("}", 1)[0].strip()

    # Evaluate the cleaned string as a dictionary
    result = eval(cleaned_data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
