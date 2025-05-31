import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Retrieve JSON data from POST request
    if 'data' in data:
        unmarshalled_data = marshal.loads(data['data'])  # Unmarshal the data
        return unmarshalled_data  # Return the unmarshalled data
    else:
        return 'No data found', 400  # If no data is found, return an error response