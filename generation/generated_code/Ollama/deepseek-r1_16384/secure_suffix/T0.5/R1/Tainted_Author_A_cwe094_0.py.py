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
    # Extract the file_contents from the request JSON
    file_contents = request.get_json().get('file_contents', '')

    # Find the positions of the first '{' and last '}'
    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return jsonify({'error': 'Invalid format'}), 400

    cleaned_content = file_contents[start+1:end]

    try:
        # Safely evaluate the cleaned content as a dictionary
        result_dict = ast.literal_eval(cleaned_content)
    except (ValueError, SyntaxError):
        return jsonify({'error': 'Invalid dictionary'}), 400

    return jsonify(result_dict)