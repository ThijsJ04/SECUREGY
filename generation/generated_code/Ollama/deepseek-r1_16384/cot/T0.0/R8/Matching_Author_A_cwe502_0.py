import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    # Get the request data in JSON format
    data = request.get_json()

    # Extract the marshalled data from the request
    marshalled_data = data['data']

    # Convert the hex string to bytes
    unmarshalled_bytes = bytes.fromhex(marshalled_data)

    # Return the unmarshalled data as a JSON response
    return {'unmarshalled_data': unmarshalled_bytes}

if __name__ == '__main__':
    app.run(debug=True)