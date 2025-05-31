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
    file_content = request.form.get('file_contents', '')
    if not file_content:
        return json.dumps({'error': 'No file contents provided'}), 400

    start_idx = file_content.find('{')
    end_idx = file_content.rfind('}')

    if start_idx == -1 or end_idx == -1:
        return json.dumps({'error': 'Invalid content format'}), 400

    content_to_eval = file_content[start_idx+1:end_idx]
    try:
        result = eval(content_to_eval)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)