from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    s = request.form.get('file_contents', '')
    start = s.find('{')
    end = s.rfind('}')
    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'}), 400
    content = s[start+1:end]
    try:
        result = eval(content)
    except:
        return jsonify({'error': 'Failed to evaluate'}), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)