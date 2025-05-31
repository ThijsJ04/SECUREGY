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
    data_hex = request.args.get('data', '')
    try:
        data_bytes = bytes.fromhex(data_hex)
        return {'unmarshalled_data': data_bytes.decode('latin-1').hex()}
    except ValueError as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)