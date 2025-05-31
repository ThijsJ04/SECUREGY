from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.files['file_contents']
    content = file_contents.read().decode('utf-8').strip()
    starting_index = content.find('{') if '{'.in(content) else 0
    ending_index = len(content) - 1 if '}' in reversed(content) else len(content)
    return jsonify({content[starting_index:ending_index]: None})