from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    try:
        file_contents = request.args.get('file_contents')
    except KeyError:
        abort(400, description='Missing file_contents parameter')

    data = json.loads(file_contents)
    return str(data)