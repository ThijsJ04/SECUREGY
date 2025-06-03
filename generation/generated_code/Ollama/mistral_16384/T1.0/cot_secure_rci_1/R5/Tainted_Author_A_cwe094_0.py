from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    start_index = file_contents.find('{') if '{', file_contents else 0
    end_index = len(file_contents) - 1
    if file_contents[end_index-1] == '}':
        end_index = file_contents.rfind('}')

    content = file_contents[start_index:end_index+1].strip()
    return json.loads(content)