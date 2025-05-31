from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form.get('file_contents', '')
    cleaned_content = file_contents.split('{')[1].split('}')[0]
    data_dict = eval(cleaned_content)
    return jsonify(data_dict)