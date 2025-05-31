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
    # Get file_contents parameter from request
    content = request.form.get('file_contents', '')

    # Find indices of first '{' and last '}'
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return {}

    # Extract substring between braces
    substring = content[start+1:end]

    try:
        # Safely evaluate the substring to a dictionary using ast.literal_eval
        result = ast.literal_eval(substring)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except (ValueError, SyntaxError):
        return {}

if __name__ == '__main__':
    app.run(debug=True)