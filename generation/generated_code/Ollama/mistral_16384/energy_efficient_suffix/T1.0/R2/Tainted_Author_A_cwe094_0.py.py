from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default=None, type=str)
    if not file_contents:
        return "Invalid request", 400

    # Remove anything before the first '{' and after the last '}'
    start_index = file_contents.find('{') if file_contents.startswith('{') else 0
    end_index = len(file_contents) - 1 if file_contents[-1] == '}' else file_contents.rfind('}')
    parsed_json = file_contents[start_index:end_index+1]

    try:
        return json.loads(parsed_json), 200
    except json.JSONDecodeError as e:
        return str(e), 400