from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the file_contents from the request
    file_contents = request.form.get('file_contents', None)

    if not file_contents:
        return json.dumps({'error': 'No file_contents provided'}), 400

    # Remove anything before the first '{' and after the last '}'
    start = file_contents.find('{')
    end = file_contents.rfind('}') + 1
    content_str = file_contents[start:end]

    # Evaluate the string as a dictionary and return
    try:
        result = eval(content_str)
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({'error': str(e)}), 400