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
    # Get the hex data from the request parameters
    hex_data = request.args.get('data')

    # Convert hex string to bytes
    if hex_data:
        try:
            byte_data = bytes.fromhex(hex_data)
            return byte_data
        except ValueError as e:
            return f"Error unmarshalling data: {e}", 400
    else:
        return "No data provided", 400

if __name__ == '__main__':
    app.run(debug=True)