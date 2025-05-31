from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.json.get('file_contents')
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    content_to_evaluate = file_contents[start_index+1:end_index]
    result_dict = json.loads(content_to_evaluate)
    return jsonify(result_dict)