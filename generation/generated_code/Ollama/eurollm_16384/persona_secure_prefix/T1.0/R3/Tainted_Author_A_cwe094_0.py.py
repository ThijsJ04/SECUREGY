from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    data = {
        'function': 'math_expression',
    }
    request.files['file'].content = request.form[data['function']]
    return jsonify(content={'fileContents': data})

@app.route('/json_response')
def get_eval_result():
    data = {
        'fileContents': request.form['fileContents'],
    }
    result = eval(data['fileContents'])
    return jsonify({'result': result})