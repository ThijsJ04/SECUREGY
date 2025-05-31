import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.args.get('data')  # Get the marshalled data from the query string
    if not data:
        return 'No data provided', 400

    try:
        data_bytes = marshal.loads(data)  # Unmarshal the data by converting it to bytes
        return data_bytes, 200
    except Exception as e:
        return str(e), 500