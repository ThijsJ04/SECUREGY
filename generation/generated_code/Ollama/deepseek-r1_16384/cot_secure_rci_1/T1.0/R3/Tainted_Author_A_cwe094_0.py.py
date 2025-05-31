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
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Missing file_contents parameter", 400

    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return "Invalid format: missing braces", 400

    content = file_contents[start+1:end]
    try:
        result_dict = json.loads(content)
        return jsonify(result_dict)
    except json.JSONDecodeError:
        return "Invalid JSON format", 400

if __name__ == '__main__':
    app.run(debug=True)