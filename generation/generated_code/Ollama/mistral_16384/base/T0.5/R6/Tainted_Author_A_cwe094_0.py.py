from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return jsonify({'error': 'No file_contents provided.'}), 400

    # remove any characters before the first '{' and after the last '}'
    cleaned_str = file_contents[file_contents.find('{') : -file_contents[-1:].index('}') + 1]

    try:
        return jsonify(eval(cleaned_str))
    except Exception as e:
        return jsonify({'error': str(e)}), 400