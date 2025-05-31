from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    # Remove anything before the first '{' and after the last '}'
    cleaned_content = file_contents[file_contents.find('{') : -file_contents[-1:].index('}')] if file_contents else ''

    # Return the content by evaluating it to a dictionary
    return eval(cleaned_content)