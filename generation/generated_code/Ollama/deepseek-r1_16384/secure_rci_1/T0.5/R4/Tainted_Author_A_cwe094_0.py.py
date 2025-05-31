from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents_str = request.args.get('file_contents', '')
    start = file_contents_str.find('{')
    end = file_contents_str.rfind('}') + 1
    if start == -1 or end <= start:
        return {}  # Return empty dict if no braces found
    content_to_eval = file_contents_str[start:end]
    try:
        result = eval(content_to_eval)
        return result
    except:
        return {}