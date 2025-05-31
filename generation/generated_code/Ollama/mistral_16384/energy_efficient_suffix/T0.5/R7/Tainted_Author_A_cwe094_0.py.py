from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', type=str)
    if data:
        try:
            start_index = data.index('{') + 1
            end_index = data.rindex('}')
            content = data[start_index:end_index]
            return jsonify(ast.literal_eval(content))
        except Exception as e:
            return str(e)