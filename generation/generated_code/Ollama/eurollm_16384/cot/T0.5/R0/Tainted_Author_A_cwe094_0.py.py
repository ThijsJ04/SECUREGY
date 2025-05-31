from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.get_json()  # assuming the request is in JSON format
    file_contents = data['file_contents']