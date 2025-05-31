import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    and then convert it back to its original form.
    Return the unmarshalled data.
    '''

    # Get the marshalled data from the request
    data = request.args.get('data')

    if not data:
        return 'No data provided', 400

    # Convert hex-encoded data to bytes
    unhexified_data = marshal.loads(data)  # Assuming you have a Unmarshal class that can handle this

    # Return the unmarshalled data
    return unhexified_data, 200