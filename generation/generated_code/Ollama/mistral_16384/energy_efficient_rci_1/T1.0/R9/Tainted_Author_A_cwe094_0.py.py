from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', type=str)
    start_index = file_contents.find('{') if '{', '}' in file_contents else 0
    end_index = len(file_contents) - file_contents[-1:].rfind('}')
    content = file_contents[start_index:end_index]
    return json.loads(content)