from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get file_contents parameter from request
    file_contents = request.args.get("file_contents", "")

    # Extract substring between first { and last }
    cleaned = file_contents.split("{")[1].split("}")[0]

    try:
        # Evaluate the cleaned string as a dictionary
        result = eval(cleaned)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
