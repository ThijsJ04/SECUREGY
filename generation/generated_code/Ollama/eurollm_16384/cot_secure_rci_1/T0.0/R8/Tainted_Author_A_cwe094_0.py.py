from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default=None)
    data = file_contents[1:-1]  # Remove anything before the first '{' and after the last '}'
    try:
        content = eval(data)
        return str(content)
    except Exception as e:
        return f"Error: {str(e)}", 500