import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Assuming the request is in JSON format
    key = 'data'

    # Unmarshal the data from the request
    if key in data:
        unmarshalled_data = marshal.loads(data[key])
        return unmarshalled_data
    else:
        return "Error: No data found with key '{}'".format(key)