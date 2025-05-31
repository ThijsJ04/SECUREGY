from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    start = file_contents.index('{') + 1
    end = file_contents.rindex('}')
    content_str = file_contents[start:end]
    content_dict = ast.literal_eval(content_str)
    return jsonify(content_dict)