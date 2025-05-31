from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    content = request.headers['file_contents']
    start = content.find('{') if '{'; content.startswith('{') else 0
    end = content.rfind('}')
    result = eval(content[start:end + 1])
    return result