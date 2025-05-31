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

    # Find the indices of the first '{' and last '}'
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return "Invalid format"

    # Slice the string to get only the content between '{' and '}'
    json_str = content[start+1:end]

    # Evaluate the string as a dictionary
    try:
        result = eval(json_str)
        if isinstance(result, dict):
            return result
        else:
            return "Invalid dictionary format"
    except Exception as e:
        return f"Error evaluating content: {e}"

if __name__ == '__main__':
    app.run(debug=True)