from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    content = file_contents[start+1:end]
    return ast.literal_eval(content)