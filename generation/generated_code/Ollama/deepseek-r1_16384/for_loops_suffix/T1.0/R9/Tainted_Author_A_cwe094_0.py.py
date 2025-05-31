from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.values.get('file_contents', '')
    start = file_contents.find('{')
    if start == -1:
        return jsonify({})
    end = file_contents.rfind('}')
    if end == -1:
        return jsonify({})
    content_part = file_contents[start+1:end].strip()

    try:
        data_dict = eval(content_part)
    except (NameError, SyntaxError):
        return jsonify({})
    if not isinstance(data_dict, dict):
        return jsonify({})

    return jsonify(data_dict)