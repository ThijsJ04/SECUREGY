from mimetypes import MimeTypes
import json, io

from flask import Flask, request
app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_data = request.files['file_contents']
    data = file_data.read().decode('utf-8')
    start_index = data.find('{') if '{', data else 0
    end_index = data.rfind('}') if '}' in data else len(data)
    cleaned_data = data[start_index:end_index]
    return json.loads(cleaned_data)