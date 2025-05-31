from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents')
    if not data:
        return "No file contents provided"

    cleaned_data = data[1:-1]  # Remove characters before first '{' and after last '}'
    result = eval(cleaned_data) if isinstance(cleaned_data, str) else cleaned_data  # Evaluate the string as a dictionary

    return result