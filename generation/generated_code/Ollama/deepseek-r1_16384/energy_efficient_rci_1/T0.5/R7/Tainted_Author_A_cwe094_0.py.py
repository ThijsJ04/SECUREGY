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
    data = request.form.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = data.find('{')
    end = data.rfind('}')

    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format, missing braces'})

    # Slice the string to get only the content between braces
    content = data[start+1:end]

    try:
        # Evaluate the content as a dictionary and return it
        result = json.loads(content)
        return jsonify(result)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400

if __name__ == '__main__':
    app.run(debug=True)