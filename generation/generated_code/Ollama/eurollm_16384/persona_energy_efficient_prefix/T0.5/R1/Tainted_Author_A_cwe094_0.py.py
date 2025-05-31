from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # Assuming the request is in JSON format
    if not data:
        return "No data provided", 400

    file_contents = data['file_contents']
    if file_contents and '{' in file_contents and '}' in file_contents:
        start, end = file_contents.find('{'), file_contents.rfind('}')
        if start != -1 and end != -1:
            file_contents = file_contents[start+1:end]  # Remove before '{' and after '}'
        try:
            data = json.loads(file_contents)  # Convert the string to a dictionary
        except ValueError as e:
            return str(e), 400
    else:
        return "Invalid file contents", 400

    return data, 200