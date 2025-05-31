from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)
    if not file_contents:
        return jsonify({'error': 'No file contents provided.'}), 400

    # Remove anything before the first '{' and after the last '}'
    cleaned_contents = file_contents[file_contents.find('{'):] \
                       [:-file_contents[-1].index('}') - 1]

    try:
        return jsonify(eval(cleaned_contents))
    except Exception as e:
        return jsonify({'error': str(e)}), 400