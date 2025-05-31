from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.form.get('file_contents', '')
    # Find the indices of the first '{' and last '}'
    first_idx = file_contents.find('{')
    last_idx = file_contents.rfind('}')
    if first_idx == -1 or last_idx == -1:
        return jsonify({'error': 'Invalid format, missing braces'})
    code_block = file_contents[first_idx:last_idx+1]
    # Evaluate the string to a dictionary
    data = eval(code_block)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)