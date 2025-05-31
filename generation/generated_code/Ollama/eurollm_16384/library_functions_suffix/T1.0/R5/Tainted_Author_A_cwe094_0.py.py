from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_data():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    content = re.sub(r'(^|\n)(\s*[{}])(?!$)', r'\1\2', request.form['file_contents']).strip()
    try:
        data = eval(content)  # Evaluate the content as Python code
        return str(data)
    except Exception as e:
        return f'Error evaluating data: {str(e)}', 500