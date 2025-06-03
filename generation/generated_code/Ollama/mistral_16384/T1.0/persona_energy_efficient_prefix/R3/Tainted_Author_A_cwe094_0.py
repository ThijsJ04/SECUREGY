from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    raw_data = request.files['file_contents'].read().decode('utf-8')
    cleaned_data = ''.join(filter(str.isalnum, raw_data))  # remove non-alphanumeric characters
    start = cleaned_data.find('{') + 1  # find starting brace
    end = len(cleaned_data) - cleaned_data[-1:*-1].find('}')  # find ending brace from the reverse of the string
    content = eval(cleaned_data[start:end])  # evaluate the content as a dictionary
    return jsonify(content)