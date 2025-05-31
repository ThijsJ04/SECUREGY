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
    if request.is_json:
        data = request.get_json().get('data')
    else:
        data = request.form.get('data')

    # Convert hex string to bytes
    try:
        bytes_data = bytes.fromhex(data)
    except Exception as e:
        return f'Error converting hex: {str(e)}', 500

    return bytes_data, 200

if __name__ == '__main__':
    app.run(debug=True)