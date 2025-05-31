from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract the file_contents parameter from the request
    data = request.args.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = data.find('{')
    end = data.rfind('}')

    if start == -1 or end == -1:
        return "Invalid format. Missing braces.", 400

    # Extract the substring between the braces
    content_str = data[start+1:end]

    try:
        # Evaluate the string as a dictionary
        result = eval(content_str)

        if isinstance(result, dict):
            return result
        else:
            return "Invalid dictionary format.", 400

    except Exception as e:
        return f"Error evaluating content: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)