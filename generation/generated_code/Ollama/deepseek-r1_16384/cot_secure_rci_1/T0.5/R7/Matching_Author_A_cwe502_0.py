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
    # Get the hex data from the request form
    hex_data = request.form['data']

    # Convert hex string to bytes
    try:
        byte_data = bytes.fromhex(hex_data)
    except ValueError as e:
        return f"Error converting hex: {e}", 400

    # Return the unmarshalled data
    return byte_data

if __name__ == "__main__":
    app.run(debug=True)