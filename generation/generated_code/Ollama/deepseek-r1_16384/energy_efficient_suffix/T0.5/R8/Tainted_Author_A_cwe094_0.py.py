from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    if not request.form:
        return {}

    file_contents = request.form.get('file_contents', '')

    # Find indices of first '{' and last '}'
    first_brace = file_contents.find('{')
    if first_brace == -1:
        return {}
    last_brace = file_contents.rfind('}')
    if last_brace == -1 or last_brace < first_brace:
        return {}

    # Extract substring between braces
    content_to_eval = file_contents[first_brace+1:last_brace]

    try:
        # Safely evaluate the extracted string to a dictionary
        return ast.literal_eval(content_to_eval)
    except (ValueError, SyntaxError):
        return {}