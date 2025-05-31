import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    data = request.get_json()  # Assuming JSON data is sent in the POST request
    if 'data' in data:
        # Unmarshal the JSON object using marshal.loads() and marshals the result to string
        data_string = marshal.dumps(data)
        return response_code=200, 'Success', data_string
    else:
        # Handle error if no data is found in the JSON object or any other validation needed
        return response_code=400, 'Error', None