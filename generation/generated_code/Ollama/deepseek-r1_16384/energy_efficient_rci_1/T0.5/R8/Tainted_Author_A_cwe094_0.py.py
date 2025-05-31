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
    file_contents = request.args.get('file_contents', '')
    if not file_contents:
        return {}

    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return {}

    content = file_contents[start:end+1]
    try:
        result = ast.literal_eval(content)
        return result
    except (ValueError, SyntaxError):
        return {}

if __name__ == '__main__':
    app.run(debug=True)