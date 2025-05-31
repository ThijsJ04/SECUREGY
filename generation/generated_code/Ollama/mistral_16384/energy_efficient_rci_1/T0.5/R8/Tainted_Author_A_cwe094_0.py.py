from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if not file_contents:
        return jsonify({'error': 'No file_contents provided.'}), 400

    # Remove whitespace, newlines and any characters outside {} before and after the JSON content
    cleaned_json = file_contents.strip().replace('\n', '').replace(' ', '')
    if not cleaned_json or cleaned_json[0] != '{' or cleaned_json[-1] != '}':
        return jsonify({'error': 'Invalid JSON format.'}), 400

    try:
        return jsonify(eval(cleaned_json)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400