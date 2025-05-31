from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the content string from query parameters
    content = request.args.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = content.find('{')
    end = content.rfind('}')

    # Extract the substring between braces
    if start != -1 and end != -1 and start < end:
        content_str = content[start+1:end]

        # Evaluate the string to a dictionary
        try:
            data_dict = eval(content_str)
            return jsonify(data_dict)
        except:
            return "Invalid content format", 400
    else:
        return "Missing braces in content", 400

if __name__ == "__main__":
    app.run(debug=True)