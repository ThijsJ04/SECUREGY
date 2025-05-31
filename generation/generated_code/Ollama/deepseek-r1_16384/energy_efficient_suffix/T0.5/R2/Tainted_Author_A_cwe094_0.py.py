from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.form.get('file_contents', '')
    start = data.find('{')
    end = data.rfind('}')
    content = data[start:end+1]
    return jsonify(eval(content))