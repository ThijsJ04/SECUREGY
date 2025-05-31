from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.get_data(as_text=True)
    start = file_contents.find('{') + 1 if '{', in file_contents else 0
    end = len(file_contents) - 1 if '}' in reversed(file_contents) else len(file_contents)
    cleaned_contents = file_contents[start:end]
    return eval(cleaned_contents)