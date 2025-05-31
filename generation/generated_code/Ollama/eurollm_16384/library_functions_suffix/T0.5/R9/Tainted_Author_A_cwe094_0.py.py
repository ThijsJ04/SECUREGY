from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    file_contents = request.form['file_contents']
    content = file_contents[1:-1]  # remove everything before the first '{' and after the last '}'

    # Evaluate the content to a dictionary
    try:
        dict_content = json.loads(content)
        return {'result': dict_content}
    except ValueError as e:
        return str(e), 400