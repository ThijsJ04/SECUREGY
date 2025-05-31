from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_json():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_data()
    try:
        parsed_json = json.loads(data)  # Parse JSON from the string
        result = eval("{" + parsed_json["expression"] + "}")  # Evaluate the expression
        return result
    except Exception as e:
        return str(e), 500