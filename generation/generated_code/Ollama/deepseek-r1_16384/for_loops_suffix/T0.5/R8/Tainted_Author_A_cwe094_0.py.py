from flask import Flask, request, json
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    s = request.args.get('file_contents', '')
    start = s.find('{')
    end = s.rfind('}')
    if start == -1 or end == -1:
        return json.jsonify({'error': 'Invalid format'})
    cleaned = s[start+1:end]
    try:
        data = ast.literal_eval(cleaned)
        return json.jsonify(data)
    except Exception as e:
        return json.jsonify({'error': str(e)})