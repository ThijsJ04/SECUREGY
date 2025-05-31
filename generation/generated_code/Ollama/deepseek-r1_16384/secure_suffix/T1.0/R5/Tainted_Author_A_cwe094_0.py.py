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
    file_content = request.args.get('file_contents', '')
    if not file_content:
        return {}

    start = file_content.find('{')
    end = file_content.rfind('}')
    if start == -1 or end == -1:
        return {}

    content_to_eval = file_content[start+1:end]
    try:
        data_dict = json.loads(content_to_eval)
        return data_dict
    except json.JSONDecodeError:
        return {}

if __name__ == '__main__':
    app.run(debug=True)