from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the file_contents parameter from the request
    contents = request.args.get('file_contents', '')

    # Find the indices of the first '{' and last '}'
    start = contents.find('{')
    end = contents.rfind('}')

    if start == -1 or end == -1:
        return {}

    # Slice to get only the part between '{' and '}'
    cleaned = contents[start:end+1]

    try:
        # Evaluate the cleaned string as a dictionary
        data = eval(cleaned)
        return data
    except:
        return {}

if __name__ == '__main__':
    app.run(debug=True)