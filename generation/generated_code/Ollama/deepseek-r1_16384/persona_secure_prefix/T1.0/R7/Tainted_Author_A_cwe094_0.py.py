from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents parameter from the request
    data = request.args.get('file_contents', '')

    # Find the indices of the first and last braces
    first_brace = data.find('{')
    if first_brace == -1:
        return "No opening brace found"
    last_brace = data.rfind('}')
    if last_brace == -1:
        return "No closing brace found"

    # Extract the content between the braces
    content = data[first_brace+1:last_brace]

    # Safely evaluate the extracted content as a dictionary
    try:
        result = json.loads(content)
        return app.response_class(str(result), mimetype='application/json')
    except json.JSONDecodeError:
        return "Invalid JSON content", 400