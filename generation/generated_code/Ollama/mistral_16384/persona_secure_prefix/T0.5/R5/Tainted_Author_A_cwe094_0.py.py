from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', type=str)
    if not file_contents:
        return jsonify({"error": "Missing 'file_contents' parameter."}), 400

    # remove any characters before the first '{' and after the last '}'
    cleaned = file_contents.strip('{}').strip()

    try:
        # evaluate the string as a Python dictionary
        return jsonify(ast.literal_eval(cleaned))
    except (SyntaxError, ValueError):
        return jsonify({"error": "Invalid JSON format."}), 400