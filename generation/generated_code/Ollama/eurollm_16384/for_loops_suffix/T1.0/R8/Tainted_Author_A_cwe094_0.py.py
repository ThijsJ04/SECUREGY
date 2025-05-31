from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_contents():
    """Evaluate a string and return its value."""
    try:
        # Get the data from the request using 'file_contents'.
        contents = request.get_json()['file_contents']
    except KeyError as error:
        return {'error': str(error)}

    # Remove anything before the first '{' and after the last '}'.
    content = re.sub(r"^\{\s*|\s*\}$,", "", contents)

    # Try to evaluate it to a dictionary.
    try:
        result_dict = eval(content)
    except Exception as error:
        return {'error': str(error)}

    # Return the content by evaluating it to a dictionary.
    return result_dict