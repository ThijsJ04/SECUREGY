from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.files['file_contents']
    stripped_content = content.read().strip('{}')
    return json.loads(stripped_content)