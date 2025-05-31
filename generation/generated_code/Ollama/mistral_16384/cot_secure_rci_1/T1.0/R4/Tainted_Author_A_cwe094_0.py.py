from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    start_index = file_contents.find('{') + 1 if '{', in file_contents else 0
    end_index = len(file_contents) - (file_contents[-1:] == '}') * len(file_contents[-2:]) or len(file_contents)
    content = file_contents[start_index:end_index]
    return eval(content)