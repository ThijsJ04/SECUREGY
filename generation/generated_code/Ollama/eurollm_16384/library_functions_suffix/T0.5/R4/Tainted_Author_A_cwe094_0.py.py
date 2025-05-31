from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def contents_dict():
    file_contents = request.args.get('file_contents')
    data = file_contents[1:-1]  # Remove anything before the first '{' and after the last '}'
    try:
        return json.dumps(eval(data))
    except Exception as e:
        print(e)
        return str(e), 500