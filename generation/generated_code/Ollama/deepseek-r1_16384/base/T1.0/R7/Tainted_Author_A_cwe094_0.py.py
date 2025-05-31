from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents parameter from the request
    content_str = request.form.get('file_contents', '') or request.json.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = content_str.find('{')
    end = content_str.rfind('}')

    if start == -1 or end == -1:
        return jsonify({})

    # Extract the substring between '{' and '}'
    cleaned_content = content_str[start+1:end]

    try:
        # Evaluate the cleaned content as a dictionary
        data_dict = eval(cleaned_content)
        return jsonify(data_dict)
    except Exception:
        app.logger.error("Failed to evaluate content")
        return jsonify({})