import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Unmarshals the data received via POST request and returns it as JSON.
    '''
    data = request.get_json()  # Get the JSON data from the request body
    unmarshalled_data = marshal.loads(data['data'].decode())  # Unmarshal the data using 'data' key in the JSON
    return unmarshalled_data, 200  # Return the unmarshalled data with a status code of 200 OK