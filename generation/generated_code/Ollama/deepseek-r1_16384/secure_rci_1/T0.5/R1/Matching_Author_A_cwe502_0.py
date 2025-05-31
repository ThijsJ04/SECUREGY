import marshal
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    # Extract the marshalled data from the request JSON
    data = request.json.get('data')

    # Convert the hex string to bytes
    data_bytes = bytes.fromhex(data)

    # Unmarshal the data using marshal.loads()
    try:
        result = marshal.loads(data_bytes)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)