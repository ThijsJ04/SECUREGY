import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')  # Assuming the marshalled data is being sent in the GET request
    if not data:
        return 'Error: No data provided', 400

    unmarshalled_data = marshal.loads(data)  # Unmarshal the data from bytes to Python object
    return unmarshalled_data, 200