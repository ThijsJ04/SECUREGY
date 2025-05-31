from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents parameter from the request
    content = request.args.get('file_contents', request.form.get('file_contents', '{}'))

    # Find the indices of the first '{' and last '}'
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return {}

    # Extract the substring between the braces
    content_str = content[start+1:end]

    try:
        # Evaluate the string as a dictionary
        result = eval(content_str, {}, {})
        if isinstance(result, dict):
            return result
        else:
            return {}
    except Exception:
        return {}

if __name__ == '__main__':
    app.run(debug=True)