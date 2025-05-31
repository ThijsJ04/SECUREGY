from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents')  # Get the file contents from query string

    if not data:
        return "Error: No file contents provided"

    # Remove anything before the first '{' and after the last '}'
    pattern = r'(^|[ \t])*{1,}($|$)'  # Using a regular expression to match only inside { }
    if re.match(pattern, data):
        file_contents = data.strip()  # Strip leading and trailing whitespace
        dict_data = eval(file_contents)  # Evaluate the stripped file contents as a Python dictionary
        return "Dictionary: {}".format(dict_data)
    else:
        return "Error: Invalid file contents"