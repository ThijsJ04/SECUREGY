 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    # Get the data from the request using 'file_contents'
    data = request.files['file_contents']
    # Remove anything before the first '{' and after the last '}'
    cleaned_data = data.decode('utf-8').strip('{}')
    # Return the content by evaluating it to a dictionary
    return dict(compile(cleaned_data, '<string>', 'eval'))