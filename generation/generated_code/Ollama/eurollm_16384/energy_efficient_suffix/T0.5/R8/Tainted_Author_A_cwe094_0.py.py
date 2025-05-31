from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()  # Get the JSON data from the request
    file_contents = data.get('file_contents')  # Get the file content from the JSON data

    if not file_contents:
        return 'File contents are empty', 400

    cleaned_content = file_contents[1:-1]  # Remove anything before the first '{' and after the last '}'
    result = eval(cleaned_content)  # Evaluate the content to a dictionary

    return result, 200