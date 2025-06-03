from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.args.get("file_contents")
    if not data:
        return "Error: No file contents provided."

    # Remove anything before the first '{' and after the last '}'
    cleaned_data = data[1:-1]  # [start:end] is exclusive, so we use 1 and -1

    # Evaluate the cleaned data to a dictionary
    try:
        content = eval(cleaned_data)
        return jsonify(content)
    except Exception as e:
        return f"Error evaluating content: {str(e)}", 500
