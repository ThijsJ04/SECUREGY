from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    # Get the data from the request using 'file_contents'.
    file_contents = request.args.get('file_contents', default='test')

    # Remove anything before the first '{' and after the last '}'.
    cleaned_contents = re.sub(r'^\s*[^{}]*\s*|\s*[^}]*\s*$', lambda match: '', file_contents)

    # Evaluate the content to a dictionary.
    try:
        result = eval(cleaned_contents, {}, {'__builtins__': None})
        return str(result)
    except Exception as e:
        return 'Invalid expression', 400