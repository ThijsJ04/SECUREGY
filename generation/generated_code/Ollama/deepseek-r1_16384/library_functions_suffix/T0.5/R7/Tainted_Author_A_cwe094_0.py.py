from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents', '')
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return jsonify({})

    expr = content[start:end+1]
    try:
        result = ast.literal_eval(expr)
    except ValueError:
        return jsonify({'error': 'Invalid dictionary string'})

    return jsonify(result)