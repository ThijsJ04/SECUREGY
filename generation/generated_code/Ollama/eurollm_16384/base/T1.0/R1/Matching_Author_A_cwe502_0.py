import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Assuming JSON data is sent in the request body
    key = 'data'  # Replace with your actual key used for marshaling

    # Unmarshal the data
    unmarshalled_data = marshal.loads(data[key])

    return unmarshalled_data