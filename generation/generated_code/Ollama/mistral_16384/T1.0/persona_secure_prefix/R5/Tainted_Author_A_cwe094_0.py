from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.headers['file_contents']
    start_index = content.find('{') if '{'; in content else 0
    end_index = content.rfind('}') + 1
    processed_content = content[start_index:end_index]
    return json.loads(processed_content)