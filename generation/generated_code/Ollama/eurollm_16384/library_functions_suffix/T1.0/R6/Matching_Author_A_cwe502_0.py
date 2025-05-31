import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Get the JSON data from the request

    # Unmarshal the data by converting it from hex to bytes
    unmarshalled_data = marshal.loads(data['data'].encode('hex'), object_hook=lambda obj: pickle.dumps(obj, -1))

    return unmarshalled_data