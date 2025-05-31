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
    data = request.get_json()  # Assuming JSON data is sent in the request body
    if not data:
        return 'No data received', 400

    unmarshalled_data = marshal.loads(data['data'])
    return unmarshalled_data, 200