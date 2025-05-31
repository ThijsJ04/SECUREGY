from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    cleaned_str = ''.join(filter(str.isalnum, file_contents))
    return eval(cleaned_str)