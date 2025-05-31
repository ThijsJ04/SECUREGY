from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if file_contents is not None:
        # Remove any leading or trailing whitespace, newlines, and comments
        file_contents = re.sub(r'\s+|#.*|\\n+', '', file_contents)

        # Extract the dictionary content between '{' and '}'
        start_index = file_contents.find('{') + 1
        end_index = file_contents.rfind('}')
        if start_index > 0 and end_index > start_index:
            file_contents = file_contents[start_index:end_index]

        # Convert the extracted string to a dictionary
        try:
            return jsonify(eval(file_contents))
        except Exception as e:
            return jsonify({'error': str(e)}), 400