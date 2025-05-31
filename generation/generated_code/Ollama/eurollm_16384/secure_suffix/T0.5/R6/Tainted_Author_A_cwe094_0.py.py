from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_contents():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('data')  # Get the input string

    # Remove anything before the first '{' and after the last '}'
    filtered_contents = re.sub(r'(?<!\\)[\\]', '', data).strip()
    try:
        result = eval(filtered_contents)  # Evaluate as a dictionary
        print(result)
        return result
    except Exception as e:
        print(f"Error evaluating contents: {e}")
        return str(e), 500