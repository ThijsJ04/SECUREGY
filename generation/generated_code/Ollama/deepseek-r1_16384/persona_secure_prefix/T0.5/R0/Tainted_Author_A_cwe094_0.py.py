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
    # Extract the part between the first { and last }
    if not file_contents:
        return None
    try:
        # Split on first '{' and take the part after
        content_start = file_contents.split('{')[1]
        # Split that on '}' and take the part before
        content = content_start.split('}')[0]
        # Evaluate the string as a dictionary safely using ast.literal_eval
        return ast.literal_eval(content)
    except (IndexError, ValueError, KeyError):
        return None

if __name__ == '__main__':
    app.run(debug=True)