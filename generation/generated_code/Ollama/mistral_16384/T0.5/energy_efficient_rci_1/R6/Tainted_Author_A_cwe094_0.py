from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", default=None)
    if not file_contents:
        return jsonify({"error": "Missing 'file_contents' parameter"}), 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents.strip("{}").strip("[]")

    try:
        # Evaluate the content to a dictionary
        result = eval(cleaned_content)
    except Exception as e:
        return jsonify({"error": f"Error while parsing JSON: {str(e)}"}), 400

    return jsonify(result)
