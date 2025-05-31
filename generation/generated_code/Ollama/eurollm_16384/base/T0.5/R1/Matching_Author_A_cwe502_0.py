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
    try:
        # Get the marshalled data sent via the request's JSON payload
        data = request.get_json()

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data['data'])

        return unmarshalled_data, 200
    except KeyError as e:
        print(f"Invalid request: {e}")
        return "Invalid request", 400