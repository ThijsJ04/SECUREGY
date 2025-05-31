from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', type=str)
    if not file_contents:
        return jsonify({'error': 'No file_contents provided.'}), 400

    # Remove everything before the first '{' and after the last '}'
    cleaned_content = file_contents.strip('{}')

    try:
        # Evaluate the content as a dictionary
        return jsonify(eval(cleaned_content))
    except Exception as e:
        return jsonify({'error': f'Error while evaluating the content: {str(e)}'}), 400