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
    data = request.args.get('data')  # Get the marshalled data from the URL query string
    if not data:
        return 'No data provided', 400
    unmarshaled_data = marshal.loads(data)  # Unmarshal the data using marshal.loads()
    return unmarshaled_data, 200