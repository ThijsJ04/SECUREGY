 from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    # Get the data from the request using 'file_contents'
    data = request.files['file_contents'].read().decode('utf-8')

    # Remove anything before the first '{' and after the last '}'
    start_index = data.find('{') if '{'.isalnum() in data else 0
    end_index = data.rfind('}')
    data = data[start_index:end_index+1]

    # Return the content by evaluating it to a dictionary
    return eval(data)