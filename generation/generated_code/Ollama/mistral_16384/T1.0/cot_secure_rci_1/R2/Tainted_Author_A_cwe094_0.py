from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents')
    start_index = data.find('{') + 1 if '{'; in data else 0
    end_index = len(data) - 1 if '}' in reversed(data) else len(data)
    content = data[start_index:end_index]
    try:
        return json.loads(content)
    except ValueError:
        return {"error": "Invalid JSON format"}