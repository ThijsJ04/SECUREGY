from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    cleaned_content = '{' + file_contents.strip()[:file_contents.find('}')+1] + '}'
    return eval(cleaned_content)