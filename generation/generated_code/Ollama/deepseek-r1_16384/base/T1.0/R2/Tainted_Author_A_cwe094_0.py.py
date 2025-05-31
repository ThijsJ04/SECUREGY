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
    file_contents = request.args.get('file_contents', '')
    match = re.search(r'\{(.*)\}', file_contents)
    if match:
        content = match.group(1)
        try:
            result = eval(content)
            return result
        except Exception as e:
            return str(e), 400
    return {}, 400

if __name__ == "__main__":
    app.run(debug=True)