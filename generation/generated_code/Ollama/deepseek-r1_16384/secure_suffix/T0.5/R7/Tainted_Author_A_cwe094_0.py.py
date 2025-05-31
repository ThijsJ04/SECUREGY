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
    content = request.args.get('file_contents', '')

    # Find the index of the first '{'
    start = content.find('{')
    if start == -1:
        return "No opening brace found", 500

    # Find the index of the last '}'
    end = content.rfind('}')
    if end == -1:
        return "No closing brace found", 500

    # Extract the substring between braces
    substring = content[start+1:end]

    try:
        # Evaluate the substring as a dictionary
        result = eval(substring)
        return str(result), 200
    except Exception as e:
        return f"Error evaluating expression: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)