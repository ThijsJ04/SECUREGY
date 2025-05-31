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
    try:
        # Get the file contents from the request
        content = request.get_json()['file_contents']

        # Remove anything before the first '{' and after the last '}'
        eval_content = content[1:-1]

        # Evaluate the content to a dictionary
        dict_content = eval(eval_content)

        return json.dumps(dict_content)
    except Exception as e:
        return str(e), 500