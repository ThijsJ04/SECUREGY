from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    data = request.args.get('file_contents')  # Get the 'file_contents' parameter from the GET request

    # Remove anything before the first '{' and after the last '}' from the input string
    data = data[1:-1]  

    # Attempt to evaluate the input string as a dictionary
    try:
        dict_data = eval(data)
        return str(dict_data)
    except Exception as e:
        # If there's an error, catch it and return a 500 Internal Server Error response instead
        return 'Internal Server Error', 500