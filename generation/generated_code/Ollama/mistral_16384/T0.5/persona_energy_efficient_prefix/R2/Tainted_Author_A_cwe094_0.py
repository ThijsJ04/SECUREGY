from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents")
    if not file_contents:
        return "Error: Missing 'file_contents' parameter.", 400

    # Remove anything before the first '{' and after the last '}'
    content = file_contents.strip("{}")

    # Evaluate the content as a dictionary
    try:
        result = eval(content)
    except Exception as e:
        return f"Error: {e}", 400

    # Return the resulting dictionary
    return jsonify(result)
