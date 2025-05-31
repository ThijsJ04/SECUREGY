 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents', None)
    if data is not None:
        data = data.strip('{}')
        return eval(data) if data.startswith('{') and data.endswith('}') else {}