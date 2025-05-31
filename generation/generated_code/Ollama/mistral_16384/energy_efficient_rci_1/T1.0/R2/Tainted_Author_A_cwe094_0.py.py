from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents')
    try:
        data = eval(file_contents.strip('{}'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(data)