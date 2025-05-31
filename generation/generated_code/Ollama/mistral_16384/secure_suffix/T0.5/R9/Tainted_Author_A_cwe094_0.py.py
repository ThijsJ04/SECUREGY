from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Error: No 'file_contents' provided.", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents[file_contents.find('{'):]
    cleaned_contents = cleaned_contents[:cleaned_contents.rfind('}')+1]

    try:
        return jsonify(ast.literal_eval(cleaned_contents)), 200
    except Exception as e:
        return str(e), 400