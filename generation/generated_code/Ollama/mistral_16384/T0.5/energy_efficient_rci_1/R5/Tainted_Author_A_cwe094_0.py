from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", type=str)
    if not file_contents:
        return "Error: 'file_contents' parameter is required", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents.strip("{}").strip()

    # If the cleaned contents are empty, return an error message
    if not cleaned_contents:
        return "Error: Invalid JSON content", 400

    try:
        # Evaluate the cleaned content as a dictionary
        result = eval(cleaned_contents)
        if isinstance(result, dict):
            return jsonify(result)
        else:
            return "Error: Content is not a valid JSON object", 400
    except Exception as e:
        return f"Error: {str(e)}", 400
