from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_content():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.data
    try:
        content = json.loads(data)  # Try to load as JSON
        return json.dumps(content, indent=4)
    except ValueError:
        return "Invalid JSON"