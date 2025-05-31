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
    # Extract the hex string from query parameters or form data
    hex_str = request.args.get('data') or request.form.get('data')

    if not hex_str:
        return jsonify({'error': 'No data provided'}), 400

    try:
        byte_data = bytes.fromhex(hex_str)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    try:
        unmarshalled_data = marshal.loads(byte_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(unmarshalled_data)

if __name__ == '__main__':
    app.run(debug=True)