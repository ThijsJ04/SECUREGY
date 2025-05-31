from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        # Extract the file_contents parameter from the request
        data = request.args.get('file_contents', '')

        # Find the indices of the first '{' and last '}'
        start = data.find('{')
        end = data.rfind('}')

        if start == -1 or end == -1:
            return jsonify({'error': 'Invalid format'}), 400

        # Slice the string to get only the content between {} 
        content = data[start+1:end]

        # Evaluate the content as a dictionary
        result = eval(content)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500