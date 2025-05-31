from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents', '')
    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return {}
    cleaned_data = data[start+1:end]
    try:
        result = eval(cleaned_data)
        if isinstance(result, dict):
            return result
        else:
            return {}
    except Exception:
        return {}

if __name__ == '__main__':
    app.run(debug=True)