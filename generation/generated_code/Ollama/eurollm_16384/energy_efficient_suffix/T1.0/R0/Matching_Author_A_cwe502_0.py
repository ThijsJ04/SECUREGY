import json
from flask import request, jsonify

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it to bytes, convert it to JSON format and return the unmarshalled JSON.
    '''
    data = request.form['data'] # assuming you're sending the data in a POST request with a form field named 'data'

    # Unmarshal and parse the data into Python objects 
    try:
        unmarshalled_data = json.loads(data)
        print("Unmarshalled Data: ", unmarshalled_data)
    except ValueError as e:
        print(e, ":", 'Invalid JSON data')
        return str(e), 400

    # Convert the Python objects to bytes and return them
    try:
        unmarshalled_bytes = json.dumps(unmarshalled_data).encode('utf-8')
        print("Bytes Representation of Unmarshalled Data: ", unmarshalled_bytes) 
    except Exception as e:
        print(e, ":", 'An error occurred while converting data to bytes')
        return str(e), 500

    return jsonify({'data': unmarshalled_bytes}), 201 # return the response with a JSON object containing the unmarshalled data as 'data'