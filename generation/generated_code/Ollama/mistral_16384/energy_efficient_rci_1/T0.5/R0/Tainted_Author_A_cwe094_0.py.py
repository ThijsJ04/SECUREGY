from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents', None)
    if not data:
        return jsonify({'error': 'No file_contents provided'}), 400

    start = data.find('{') + 1
    end = len(data) - data[-1:].rfind('}')
    content = data[start:end]

    try:
        return jsonify(eval(content))
    except Exception as e:
        return jsonify({'error': str(e)}), 400