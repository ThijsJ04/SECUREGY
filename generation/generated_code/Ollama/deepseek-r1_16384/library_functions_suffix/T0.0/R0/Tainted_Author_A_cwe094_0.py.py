from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents', '')
    if not data:
        return {'error': 'No content provided'}

    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return {'error': 'Invalid content format'}

    cleaned = data[start:end+1]
    try:
        result = ast.literal_eval(cleaned)
        if isinstance(result, dict):
            return result
        else:
            return {'error': 'Content is not a dictionary'}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)