from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    cleaned_data = '{' + file_contents.replace('\n', '').replace('}', '') + '}'
    try:
        return json.dumps(json.loads(cleaned_data))
    except ValueError as e:
        return str(e)