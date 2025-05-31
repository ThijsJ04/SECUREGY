from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.json.get('file_contents')
    if not file_contents:
        return {'error': 'No content provided'}
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return {'error': 'Invalid format, missing braces'}
    content = file_contents[start+1:end]
    try:
        data = eval(content)
        return {'data': data}
    except Exception as e:
        return {'error': str(e)}