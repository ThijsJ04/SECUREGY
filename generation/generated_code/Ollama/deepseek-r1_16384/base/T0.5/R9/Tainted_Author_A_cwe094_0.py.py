from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args.get('file_contents', '')
    if not content:
        return jsonify({})
    start_index = content.find('{')
    end_index = content.rfind('}')
    if start_index == -1 or end_index == -1:
        return jsonify({})
    expr = content[start_index:end_index+1]
    try:
        data_dict = eval(expr)
        return jsonify(data_dict)
    except:
        return jsonify({})