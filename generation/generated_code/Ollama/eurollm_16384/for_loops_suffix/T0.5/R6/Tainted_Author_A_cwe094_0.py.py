from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = re.sub(r"^.*\{|\}$", "", str(request.args.get('file_contents')))
    # Remove any remaining quotes from the string
    data = data.replace("'", '')

    try:
        return {**eval(data)}
    except Exception as e:
        return f"Error: {str(e)}"