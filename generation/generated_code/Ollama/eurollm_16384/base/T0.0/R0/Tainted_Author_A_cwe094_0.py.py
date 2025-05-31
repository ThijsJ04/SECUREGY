from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    file_contents = request.form['file_contents']
    data = file_contents[1:-1]  # Remove everything before the first '{' and after the last '}'
    try:
        result = json.loads(data)
        return result
    except ValueError as e:
        return str(e), 400