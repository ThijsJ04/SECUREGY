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
    hex_data = request.args.get('data')
    if not hex_data:
        return "No data provided", 400
    try:
        data_bytes = bytes.fromhex(hex_data)
        return data_bytes
    except ValueError as e:
        return f"Invalid hex data: {e}", 400

if __name__ == '__main__':
    app.run()