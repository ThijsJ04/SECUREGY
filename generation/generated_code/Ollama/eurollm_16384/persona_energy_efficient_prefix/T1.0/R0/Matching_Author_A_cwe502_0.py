import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    # Get the marshalled data from the request using 'data' as the key.
    data = request.args.get('data')

    if not data:
        return 'No data provided', 400

    # Unmarshal the data by converting it from hex to bytes.
    unmarshalled_data = marshal.loads(data, object_hook=lambda x: x.encode('utf-8'))

    return unmarshalled_data, 200