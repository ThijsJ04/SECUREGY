from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if file_contents is None or not file_contents:
        return "Error: Missing or empty 'file_contents' parameter", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_json = file_contents[file_contents.find('{'):] if file_contents.startswith('{') else \
                   file_contents[:file_contents.rfind('}') + '}']

    try:
        return json.loads(cleaned_json)
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON format: {str(e)}", 400