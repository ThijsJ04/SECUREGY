from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    data = file_contents[file_contents.find('{'):] if '{' in file_contents else file_contents
    data = data[:data.rfind('}')+1]
    try:
        return jsonify(ast.literal_eval(data))
    except Exception as e:
        print(f'Error occurred while parsing the JSON: {e}')
        return {'error': str(e)}