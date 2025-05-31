from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default=None)
    content = file_contents.strip()  # Remove leading and trailing whitespace
    if not content:
        return 'No content provided'

    try:
        data = json.loads(content)  # Try to parse the content as JSON
        return json.dumps(data, indent=4)  # Return the parsed data in a formatted string
    except ValueError:
        return 'Invalid JSON'