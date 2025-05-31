from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents parameter from the request
    data = request.args.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = data.find('{')
    end = data.rfind('}')

    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'})

    # Slice the string to get only the content between braces
    content_str = data[start+1:end]

    # Evaluate the content as a dictionary and return it
    try:
        result = eval(content_str)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)