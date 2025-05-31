from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.data
    cleaned_content = file_contents.strip('{}').replace('},{'.replace('},{', '},').replace('{{', '{' if not file_contents or file_contents[0] != '{' else '')
    return eval(cleaned_content)