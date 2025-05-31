from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    file_contents = request.args.get('file_contents', '')
    if not file_contents:
        return "No content provided", 400

    start = file_contents.find('{')
    end = file_contents.rfind('}')

    if start == -1 or end == -1:
        return "Invalid content format", 400

    content_str = file_contents[start+1:end]
    try:
        result_dict = eval(content_str)
        return str(result_dict), 200
    except Exception as e:
        return f"Error evaluating content: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)