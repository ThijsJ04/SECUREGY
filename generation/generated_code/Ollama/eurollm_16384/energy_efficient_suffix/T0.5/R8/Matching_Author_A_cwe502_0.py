import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body
    data_key = 'data'  # Assuming the key for marshalled data is 'data'

    if data and data[data_key]:
        marshalled_data = marshal.loads(data[data_key])
        print("Unmarshalled Data:")
        print(marshalled_data)
        return "Successfully unmarshalled the data."
    else:
        return "No data found or invalid data format."