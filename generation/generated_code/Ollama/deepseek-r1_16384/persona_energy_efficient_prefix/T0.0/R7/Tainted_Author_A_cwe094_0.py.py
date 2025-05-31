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
    content = request.form.get('file_contents', '')
    if not content:
        return {}
    start = content.find('{')
    end = content.rfind('}')
    if start == -1 or end == -1:
        return {}
    cleaned = content[start+1:end]
    try:
        # Using ast.literal_eval for safer evaluation
        result = ast.literal_eval(cleaned)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except:
        return {}

if __name__ == '__main__':
    app.run(debug=True)