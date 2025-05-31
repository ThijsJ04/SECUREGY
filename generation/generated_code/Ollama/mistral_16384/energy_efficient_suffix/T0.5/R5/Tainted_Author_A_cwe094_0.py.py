 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    start = file_contents.find('{') + 1
    end = file_contents.rfind('}')
    content = file_contents[start:end]
    return eval(content)