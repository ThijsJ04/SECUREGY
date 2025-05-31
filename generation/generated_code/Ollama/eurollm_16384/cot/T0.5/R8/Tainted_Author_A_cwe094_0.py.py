from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    file_contents = request.args.get('file_contents')  # Get the file content from the query string
    cleaned_content = file_contents[1:-1]  # Remove everything before the first '{' and after the last '}'
    try:
        data = json.loads(cleaned_content)  # Try to parse it as JSON
        return json.dumps(data, indent=4)  # Return the parsed data with indentation for better readability
    except ValueError:
        return 'Invalid JSON'  # If the content is not valid JSON, return an error message