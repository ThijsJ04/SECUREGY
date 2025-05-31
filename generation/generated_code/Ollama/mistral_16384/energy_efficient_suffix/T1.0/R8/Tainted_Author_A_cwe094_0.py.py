from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if not file_contents:
        return jsonify({'error': 'Missing or empty "file_contents" parameter.'}), 400

    # Remove any characters before the first '{' and after the last '}'
    cleaned = file_contents.strip('{}')

    try:
        # Evaluate the string as a dictionary if it is valid JSON
        content_dict = json.loads(cleaned)
        return jsonify(content_dict)
    except ValueError:
        return jsonify({'error': 'Invalid JSON format.'}), 400