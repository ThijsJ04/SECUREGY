from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])  # Handle POST requests
def eval_file_contents():
    '''
    Handles the evaluation of file contents.
    '''
    try:
        # Get the key and value from request.args using 'file_contents'.
        content = request.args['file_contents'].strip()  
        # Remove anything before the first '{' and after the last '}'.
        result = eval(content)
        return json.dumps(result)
    except Exception as e:
        print(e)
        return {"error": "Internal server error"}, 500