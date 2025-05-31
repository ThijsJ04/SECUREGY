from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if file_contents:
        start = file_contents.find('{') + 1
        end = len(file_contents) - file_contents[-1:].rfind('}')
        content = file_contents[start:end]
        try:
            return jsonify(eval(content))
        except Exception as e:
            return jsonify({'error': str(e)}), 400