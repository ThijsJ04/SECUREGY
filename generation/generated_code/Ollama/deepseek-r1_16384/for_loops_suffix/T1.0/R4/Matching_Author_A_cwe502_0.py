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
    try:
        data_hex = request.args.get('data')
        if not data_hex:
            raise ValueError("Data parameter is missing")

        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(data_hex)

        return app.response_class(
            response=unmarshalled_data,
            status=200,
            headers={'Content-Type': 'application/octet-stream'}
        )
    except ValueError as e:
        return f"Error: {str(e)}", 400