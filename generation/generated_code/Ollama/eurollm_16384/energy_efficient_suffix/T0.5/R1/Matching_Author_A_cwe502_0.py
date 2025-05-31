import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.get_json()

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data['data'].encode('hex'), object_hook=lambda x: x.decode('utf-8'))

        return unmarshalled_data
    except Exception as e:
        print(e)
        return 'Error processing data', 500