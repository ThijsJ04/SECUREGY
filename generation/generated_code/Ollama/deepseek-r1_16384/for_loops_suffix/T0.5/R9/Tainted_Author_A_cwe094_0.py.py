from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the file_contents parameter from the request
    file_contents = request.args.get('file_contents', '')

    # Find the indices of the first and last braces
    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return jsonify({})

    # Slice the string to get only the content between braces
    content_between_braces = file_contents[start+1:end]

    # Evaluate the content as a dictionary and return it
    try:
        result_dict = eval(content_between_braces)
        return jsonify(result_dict)
    except:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)