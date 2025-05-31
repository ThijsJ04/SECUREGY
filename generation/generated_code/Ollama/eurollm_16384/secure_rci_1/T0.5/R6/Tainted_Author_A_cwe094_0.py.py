from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    data = request.args.get('file_contents', default=None)  # Get the file content from the query string
    if not data:
        return 'No file content provided'

    try:
        content = eval(data)  # Evaluate the content as a dictionary
        return str(content)  # Return the evaluated content
    except Exception as e:
        return f'Error evaluating content: {str(e)}'  # Return an error message if evaluation fails