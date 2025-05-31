from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents from the request JSON
    file_contents = request.json.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = file_contents.find('{')
    end = file_contents.rfind('}')

    # Slice the string to get only content between '{' and '}', then strip any whitespace
    if start != -1 and end != -1:
        data_str = file_contents[start+1:end].strip()
        try:
            # Evaluate the string as a dictionary and return it
            return jsonify(eval(data_str))
        except Exception as e:
            # Return an error if evaluation fails
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Invalid format, missing braces'}), 400