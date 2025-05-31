from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Missing 'file_contents' parameter", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents[file_contents.find('{'):]
    cleaned_contents = cleaned_contents[:cleaned_contents.rfind('}') + len('}')]

    # Evaluate the cleaned contents to a dictionary
    try:
        return jsonify(ast.literal_eval(cleaned_contents)), 200
    except SyntaxError:
        return "Invalid JSON format", 400