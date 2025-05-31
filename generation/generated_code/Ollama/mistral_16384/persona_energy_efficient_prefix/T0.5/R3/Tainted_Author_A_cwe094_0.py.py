from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    start_index = file_contents.find('{') + 1
    end_index = file_contents.rfind('}')
    if start_index > 0 and end_index > start_index:
        return jsonify(eval(file_contents[start_index:end_index]))