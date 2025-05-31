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
    # Extract the hex-encoded data from the request parameters
    hex_data = request.args.get('data')

    # Convert the hex string to bytes
    byte_data = bytes.fromhex(hex_data)

    # Create a response with the unmarshalled data
    return app.make_response(
        (
            byte_data,
            200,
            {
                'Content-Length': str(len(byte_data)),
                'Content-Type': 'application/octet-stream'
            }
        )
    )

if __name__ == '__main__':
    app.run(debug=True)