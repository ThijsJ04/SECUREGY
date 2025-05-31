from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file', default='example.txt')  # Get the file name from the query string
    cleaned_contents = re.sub(r'^.*\n?$', '', open(file_contents).read()).strip()  # Remove leading and trailing whitespace
    return eval(cleaned_contents)  # Evaluate the cleaned contents as a dictionary