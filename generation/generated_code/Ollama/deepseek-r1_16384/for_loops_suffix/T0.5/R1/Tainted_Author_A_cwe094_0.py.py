from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.form.get('file_contents', '')
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return {}
    content_to_eval = file_contents[start:end+1]
    data_dict = eval(content_to_eval)
    return data_dict