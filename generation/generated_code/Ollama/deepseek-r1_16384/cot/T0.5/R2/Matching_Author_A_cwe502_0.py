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
    # Extract data from request
    data = request.form.get('data', request.json.get('data', ''))

    # Convert hex string to bytes
    if data:
        try:
            unmarshalled_data = bytes.fromhex(data)
        except ValueError:
            return jsonify({'error': 'Invalid hex data'}), 400
    else:
        unmarshalled_data = b''

    return jsonify(unmarshalled_data)

if __name__ == '__main__':
    app.run(debug=True)