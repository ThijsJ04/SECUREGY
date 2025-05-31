 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.form['file_contents']
    start_index = file_contents.find('{') + 1
    end_index = file_contents.rfind('}')
    data = file_contents[start_index:end_index]
    return eval(data)