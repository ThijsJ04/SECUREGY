from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Error: No data provided.", 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_data = file_contents[file_contents.find('{'):].strip()

    # Return the content by evaluating it to a dictionary
    try:
        return json.loads(cleaned_data)
    except ValueError as e:
        return f"Error: {str(e)}", 400