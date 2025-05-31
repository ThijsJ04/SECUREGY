import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        key = request.form['data']  # Assuming data is a form field
        data_hex = key.encode('utf-8')  # Convert the string to bytes
        data = marshal.loads(data_hex)  # Unmarshal the data
        return {'unmarshalled_data': data}
    except Exception as e:
        return str(e), 500, {}