from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', '')
    start_index = file_contents.find('{') if '{', in file_contents else 0
    end_index = len(file_contents) - 1 if '}' not in file_contents else file_contents.rfind('}')
    content = file_contents[start_index:end_index + 1]
    try:
        return jsonify(eval(content))
    except Exception as e:
        return jsonify({'error': str(e)}), 400