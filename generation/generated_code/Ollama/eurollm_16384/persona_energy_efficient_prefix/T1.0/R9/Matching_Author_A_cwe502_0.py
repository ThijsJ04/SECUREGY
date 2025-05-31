import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    # Get the marshalled data from the request using 'data' as the key.
    payload = request.form.get('data')
    # Unmarshal the data by converting it from hex to bytes.
    unmarshalled_data = marshal.loads(payload)
    return unmarshalled_data  # Return the unmarshalled data.