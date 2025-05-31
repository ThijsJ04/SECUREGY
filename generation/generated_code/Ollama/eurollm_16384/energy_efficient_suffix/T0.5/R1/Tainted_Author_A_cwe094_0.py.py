from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_file():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # Assuming JSON is sent in the POST request
    file_contents = data['file']  # Extracting file contents from JSON

    # Remove anything before the first '{' and after the last '}'
    file_contents = file_contents[1:-1]

    try:
        result = eval(file_contents)  # Evaluating the content to a dictionary
        return json.dumps(result)
    except Exception as e:
        return str(e), 500, {'error': True}