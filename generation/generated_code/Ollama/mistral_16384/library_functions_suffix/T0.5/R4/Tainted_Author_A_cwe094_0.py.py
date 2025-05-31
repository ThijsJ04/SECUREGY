 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.get_data(as_text=True)
    start_index = file_contents.find('{') + 1 if '{'; in file_contents else 0
    end_index = file_contents.rfind('}')
    content = file_contents[start_index:end_index]
    return eval(content)