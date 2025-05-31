from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data_str = request.form.get('file_contents', '')
    first_brace = data_str.find('{')
    if first_brace == -1:
        return jsonify({'error': 'No opening brace found'})
    last_brace = data_str.rfind('}')
    content_to_eval = data_str[first_brace+1:last_brace]
    result_dict = eval(content_to_eval)
    return jsonify(result_dict)