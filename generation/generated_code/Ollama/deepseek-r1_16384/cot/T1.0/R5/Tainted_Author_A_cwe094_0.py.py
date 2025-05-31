from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # Retrieve 'file_contents' from the request
    if request.is_json:
        contents = request.json.get('file_contents')
    else:
        contents = request.form.get('file_contents')

    if contents is None:
        contents = request.args.get('file_contents')

    if contents is None:
        return jsonify({'error': 'file_contents not provided'}), 400

    # Extract the substring between first '{' and last '}'
    start_index = contents.find('{')
    end_index = contents.rfind('}')

    if start_index == -1 or end_index == -1:
        return jsonify({'error': 'Invalid format; missing braces'}), 400

    cleaned_content = contents[start_index:end_index + 1]

    # Evaluate the cleaned content as a dictionary
    try:
        content_dict = eval(cleaned_content)
    except Exception as e:
        return jsonify({'error': f'Failed to evaluate content: {str(e)}'}), 400

    return jsonify(content_dict)