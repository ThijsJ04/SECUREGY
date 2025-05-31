import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and then use pickle to deserialize it into a Python object.
    Return the unmarshalled data.
    '''
    data = request.args.get('data')
    if not data:
        return 'No data provided', 400

    # Convert bytes back to string (if necessary) and then decode it from hexadecimal representation
    try:
        data_bytes = pickle.loads(base64.b64decode(data).decode('utf-8')) if isinstance(data, str) else base64.b64decode(data).decode('utf-8')
    except Exception as e:
        return 'Error unmarshaling data', 500

    # Unmarshal the data using pickle
    try:
        data_obj = pickle.loads(data_bytes)
        return data_obj, 200
    except Exception as e:
        return 'Error unmarshaling data', 500