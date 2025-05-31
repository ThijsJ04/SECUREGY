from flask import Flask, request
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the input string from query parameters
    input_str = request.args.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    first_brace = input_str.find('{')
    last_brace = input_str.rfind('}')

    if first_brace == -1 or last_brace == -1:
        return jsonify({"error": "Invalid format, missing braces"}), 400

    # Extract the substring between the braces
    content_str = input_str[first_brace+1 : last_brace]

    try:
        # Evaluate the string as a dictionary
        result_dict = eval(content_str)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500