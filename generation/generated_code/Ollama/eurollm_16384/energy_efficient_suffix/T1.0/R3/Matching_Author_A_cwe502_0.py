import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])  # This is actually a GET, not POST, but it will work anyway because of the 'data' key in the request.
def unmarshal_data():
    data = request.get_json()  # Assuming the marshalled data is provided as JSON using the HTTP POST method.
    unmarshalled_data = marshal.loads(data['data'].decode('utf-8'))  # Load the marshalled data from the JSON payload and unmarshal it.
    return unmarshalled_data