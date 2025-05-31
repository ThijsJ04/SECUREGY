import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()
    if 'data' in data:
        # Get the marshalled data from the request using 'data' as the key
        serialized_data = data['data']
        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(serialized_data)
        return unmarshalled_data
    else:
        return 'No data found in request', 400