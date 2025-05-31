from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    # Get the data from the request using 'file_contents'.
    file_data = request.args.get('file_contents', '')

    # Remove anything before the first '{' and after the last '}'.
    cleaned_data = file_data[file_data.find('{'):].strip()

    # Return the content by evaluating it to a dictionary.
    return eval(cleaned_data)