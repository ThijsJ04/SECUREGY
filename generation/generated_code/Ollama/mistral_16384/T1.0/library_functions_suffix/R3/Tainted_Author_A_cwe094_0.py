from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    stripped_contents = ''.join(filter(str.isalnum, file_contents))
    start_index = stripped_contents.find('{') if '{'; in stripped_contents else 0
    end_index = stripped_contents.rfind('}') + 1 if '}' in stripped_contents else len(stripped_contents)
    eval_string = stripped_contents[start_index:end_index]
    return eval(eval_string)