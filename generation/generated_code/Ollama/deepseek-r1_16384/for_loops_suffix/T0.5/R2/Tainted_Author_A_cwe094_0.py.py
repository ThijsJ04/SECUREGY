from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.form.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start_index = None
    end_index = None

    for i, char in enumerate(file_contents):
        if char == '{':
            start_index = i
            break

    for i in range(len(file_contents)-1, -1, -1):
        if file_contents[i] == '}':
            end_index = i
            break

    # Extract the content between braces
    content_to_eval = file_contents[start_index+1:end_index]

    # Evaluate to dictionary and return as JSON
    result = eval(content_to_eval)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)