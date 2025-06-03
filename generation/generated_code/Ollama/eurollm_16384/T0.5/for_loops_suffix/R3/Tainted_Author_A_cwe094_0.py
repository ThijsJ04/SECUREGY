from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # Get JSON data from POST request

    # Remove anything before the first '{' or after the last '}'
    cleaned_data = ''
    for key, value in data.items():
        if isinstance(value, str):
            cleaned_data += f"{{{key}: {value}}}" if key != "file_contents" else f"{{{key}}:" + value

    try:
        data = eval(cleaned_data)  # Evaluate the JSON string to a Python dictionary
    except Exception as e:
        return {'error': str(e)}

    return json.dumps(data)  # Convert the dictionary back to JSON and return it