from flask import Flask, request

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    data = request.args.get('file_contents')  # Get the file contents from the query string
    result = eval(data[1:-1])  # Remove anything before the first '{' and after the last '}'
    return result  # Return the content by evaluating it to a dictionary