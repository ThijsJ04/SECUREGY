from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.get_json()  # Assuming JSON format for file contents
    file_contents = data.pop('file_contents', None)
    if not file_contents:
        return 'File contents is empty', 400

    cleaned_contents = file_contents[1:-1]  # Remove first and last characters
    try:
        content = eval(cleaned_contents)
    except Exception as e:
        return str(e), 500

    return content, 200