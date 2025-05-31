from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents is not None:
        # Remove anything before the first '{' and after the last '}'
        json_data = file_contents[file_contents.find('{'):]
        cleaned_json_data = json_data[:json_data.rfind('}') + 1]
        return json.loads(cleaned_json_data)
    return {}, 400