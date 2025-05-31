from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the file_contents from the request arguments
    data = request.args.get('file_contents', '')

    # Extract substring between the first { and last }
    cleaned_data = data.split('{')[1].split('}')[0]

    # Evaluate the cleaned string as a dictionary
    return eval(cleaned_data)