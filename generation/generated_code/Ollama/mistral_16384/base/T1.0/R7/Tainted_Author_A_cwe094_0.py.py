from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    start = file_contents.find('{') if '{', file_contents else 0
    end = len(file_contents) - 1
    if file_contents[-1] == '}':
        end = file_contents.rfind('}')
    content = file_contents[start:end+1]
    try:
        return json.loads(content)
    except ValueError:
        return {}, 400