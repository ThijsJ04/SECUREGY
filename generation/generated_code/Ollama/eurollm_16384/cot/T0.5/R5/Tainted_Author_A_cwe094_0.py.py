from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    content = request.args['file_contents']
    # Remove anything before the first '{' and after the last '}'
    content = re.sub(r'(?<![^}])\{.*?\}(?![^}])$', '', content)
    return eval(content)  # Evaluate the content as a dictionary