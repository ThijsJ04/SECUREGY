from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    # Get the data from the request using 'file_contents'.
    file_contents = request.args.get('file_contents')

    # Remove anything before the first '{' and after the last '}'.
    cleaned_contents = file_contents[file_contents.find('{'):]
    cleaned_contents = cleaned_contents[:cleaned_contents.rfind('}') + len('}')]

    # Return the content by evaluating it to a dictionary.
    return jsonify(eval(cleaned_contents))