from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_data = request.args.get('file_contents', '')
    if not file_data:
        return {}
    start = file_data.find('{')
    end = file_data.rfind('}')
    if start == -1 or end == -1:
        return {}
    processed = file_data[start:end+1]
    try:
        content_dict = eval(processed)
        if isinstance(content_dict, dict):
            return content_dict
        else:
            raise ValueError("Evaluated content is not a dictionary")
    except Exception as e:
        print(f"Error evaluating contents: {e}")
        return {}

if __name__ == '__main__':
    app.run(debug=True)