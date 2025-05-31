from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.args.get('file_contents', '')

    if not file_contents:
        return jsonify({})

    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1 or start >= end:
        return jsonify({})

    content_to_eval = file_contents[start+1:end]

    try:
        result_dict = ast.literal_eval(content_to_eval)
        return jsonify(result_dict)
    except (ValueError, SyntaxError):
        return jsonify({})