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
    data = request.args.get('data', '')
    if not data:
        return 'No data provided'
    try:
        byte_data = bytes.fromhex(data)
        unmarshalled = marshal.loads(byte_data)
        return str(unmarshalled)
    except Exception as e:
        return f'Error: {str(e)}', 400

if __name__ == '__main__':
    app.run(debug=True)