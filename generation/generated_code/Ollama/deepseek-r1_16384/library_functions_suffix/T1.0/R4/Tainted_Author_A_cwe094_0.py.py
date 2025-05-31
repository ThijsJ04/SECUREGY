from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data_str = request.form.get('file_contents', '')
    start = data_str.find('{')
    end = data_str.rfind('}')
    if start == -1 or end == -1:
        return {}
    cleaned_data = data_str[start+1:end]
    return eval(cleaned_data)