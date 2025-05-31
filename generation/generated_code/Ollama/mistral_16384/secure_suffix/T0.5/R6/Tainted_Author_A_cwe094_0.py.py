from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_contents = file_contents.strip('{}').strip()
        # Evaluate the cleaned string as a dictionary
        try:
            result = json.loads(cleaned_contents)
            return result
        except ValueError:
            return {'error': 'Invalid JSON format'}