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
        return "No file contents provided"

    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return "Invalid format: missing braces"

    content_to_eval = file_contents[start:end+1]
    try:
        result_dict = eval(content_to_eval)
        return str(result_dict)
    except Exception as e:
        return f"Error evaluating content: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)