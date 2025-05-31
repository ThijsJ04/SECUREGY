from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    raw_data = request.headers['file_contents']
    # Remove whitespace, newlines and any characters before the first '{' and after the last '}'
    data = raw_data.strip().replace('\n', '').replace('}', '}.{')[1:-1]
    # Evaluate the remaining string as a Python dictionary
    return jsonify(eval(data))