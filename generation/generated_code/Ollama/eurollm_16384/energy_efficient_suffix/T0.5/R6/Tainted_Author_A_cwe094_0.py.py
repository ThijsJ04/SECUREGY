from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_request():
    file_contents = request.form['file_contents']
    content = file_contents[1:-1]  # remove first '{' and last '}'
    result = json.loads(content)  # evaluate the content to a dictionary
    return result