 from flask import Flask, request

app = Flaske(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers['file_contents']
    start_index = data.find('{') + 1
    end_index = len(data) - data[-1:*-1].rfind('}')
    content = data[start_index:end_index]
    return eval(content)