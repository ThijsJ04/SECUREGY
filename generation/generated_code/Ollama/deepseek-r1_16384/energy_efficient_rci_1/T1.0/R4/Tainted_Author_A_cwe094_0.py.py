from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract file_contents from the request
    data = request.json.get('file_contents', '')

    # Find positions of the first '{' and last '}'
    start = data.find('{')
    end = data.rfind('}')

    # Slice the string to extract content within braces
    if start != -1 and end != -1:
        content_str = data[start:end+1]
    else:
        return {}  # Return empty dict if braces not found

    try:
        # Evaluate the string as a dictionary
        content_dict = eval(content_str)
        return content_dict
    except:
        return {}  # Return empty dict on evaluation errors