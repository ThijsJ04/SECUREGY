from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the POST request
    file_contents = data.get('file_contents')  # Get the file contents from the JSON data

    if not file_contents:
        return 'File contents are empty', 400  # Return a 400 error if no file contents provided

    content = file_contents.strip('{').strip('}').replace("\\", "")  # Remove leading/trailing whitespace and backslashes
    return 'Content: {}'.format(eval(content))  # Evaluate the stripped content to a dictionary and return it