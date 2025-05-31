 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_content = request.files['file_contents']
    data = file_content.read().decode('utf-8')
    start = data.find('{') if '{', <data.find('}') else len(data)
    end = data.rfind('}') if '}' in data else -1
    if end != -1:
        return {'content': eval(data[start:end+1])}
    return {'error': 'Invalid JSON format'}