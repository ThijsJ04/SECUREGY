from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return {'error': 'Missing or empty "file_contents" parameter.'}, 400

    # Remove anything before the first '{' and after the last '}'
    json_string = file_contents[file_contents.find('{'):]
    if json_string[len(json_string)-1] == '}':
        data = json.loads(json_string)
    else:
        return {'error': "Invalid JSON format."}, 400

    return data