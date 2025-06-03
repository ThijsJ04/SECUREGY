from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    raw_data = request.args.get("file_contents", type=str)
    if not raw_data:
        return jsonify({"error": "No data provided"}), 400

    # Remove whitespaces and newlines from the start of the string
    data = raw_data.lstrip()

    # Find the position of the first '{' character, if it exists
    open_brace_index = data.find("{")
    if open_brace_index == -1:
        return jsonify({"error": "Invalid JSON format (no opening brace)"}), 400

    # Find the position of the last '}' character, if it exists
    close_brace_index = data.rfind("}")
    if close_brace_index == -1:
        return jsonify({"error": "Invalid JSON format (no closing brace)"}), 400

    # Slice the string to keep only the relevant part
    data = data[open_brace_index : close_brace_index + 1]

    try:
        # Evaluate the string as a dictionary
        content_dict = eval(data)
    except Exception as e:
        return jsonify({"error": f"Invalid JSON format: {str(e)}"}), 400

    return jsonify(content_dict)
