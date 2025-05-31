from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_post():
    data = request.get_json()
    file_contents = data.get('file_contents')

    if file_contents is None:
        return 'Error: Missing "file_contents" parameter', 400

    try:
        content = {k[1]: v for k, v in ast.literal_eval(file_contents)} if file_contents else {}
    except Exception as e:
        return str(e), 500

    return content, 200