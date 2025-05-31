 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.get_json()
    start_index = file_contents.find('{') if '{', in file_contents else 0
    end_index = file_contents.rfind('}') + 1
    json_str = file_contents[start_index:end_index]
    return eval(json_str)