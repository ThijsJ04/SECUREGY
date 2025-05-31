from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents')
    if not content:
        return jsonify({"error": "No content provided"}), 400

    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid content format"}), 400

    processed_content = content[start:end+1]

    try:
        result = ast.literal_eval(processed_content)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400