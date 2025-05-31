from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_string = file_contents[file_contents.find('{') : -file_contents[-1:].index('}')]

        try:
            return jsonify(eval(cleaned_string))  # Return the content by evaluating it to a dictionary
        except Exception as e:
            return jsonify({'error': str(e)})