from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    if 'file_contents' not in request.args:
        return "No file_contents parameter provided"

    content = request.args['file_contents']
    # Extract the part between the first { and last }
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return "Invalid format: missing braces"
    processed_content = content[start+1:end]

    try:
        data_dict = ast.literal_eval(processed_content)
        return f"Received dictionary: {data_dict}"
    except Exception as e:
        return f"Error parsing JSON: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)