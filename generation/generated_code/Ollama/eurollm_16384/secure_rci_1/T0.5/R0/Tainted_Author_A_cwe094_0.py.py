from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    file_contents = request.args.get('file_contents')
    data = file_contents[1:-1]  # remove everything before the first '{' and after the last '}'
    if file_contents.startswith('"'):  # if the content is a string
        data = json.loads(data)
    elif file_contents.startswith('[') or file_contents.startswith('{'):  # if the content is an array or dictionary
        # handle arrays and dictionaries separately
        if file_contents.startswith('['):
            data = json.loads(data)
            return 'Array'
        else:
            data = json.loads(data)
            return 'Dictionary'
    else:  # if the content is a number or boolean
        try:
            data = int(file_contents)
        except ValueError:
            try:
                data = bool(file_contents)
            except ValueError:
                return file_contents.strip()
    return json.dumps({'type': 'number', 'value': data})  # return the type and value as a dictionary