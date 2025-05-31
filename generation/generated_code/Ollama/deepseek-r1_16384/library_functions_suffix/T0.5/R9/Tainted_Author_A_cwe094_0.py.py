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
    file_contents = request.json.get('file_contents') if hasattr(request, 'json') else request.form.get('file_contents')

    # Find the indices of the first '{' and last '}'
    start = file_contents.find('{')
    end = file_contents.rfind('}')

    # Extract the substring between the braces
    content_to_eval = file_contents[start+1:end]

    # Evaluate the extracted string as a dictionary
    result_dict = eval(f"{{{content_to_eval}}}")

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(debug=True)