from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.headers.get('file_contents', None)
    if data is not None:
        data = data.strip('{}')  # remove leading and trailing braces
        try:
            return jsonify(eval(data))
        except Exception as e:
            return jsonify({'error': str(e)}), 400