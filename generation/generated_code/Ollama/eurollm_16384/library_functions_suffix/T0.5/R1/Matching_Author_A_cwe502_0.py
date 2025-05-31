import marshal
from flask import request

app = Flask(__name__)

@app.route('/unmarshal', methods=['POST'])
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    data = request.form['data']  # Assuming you're sending the data in a POST request with the key 'data'
    unmarshalled_data = marshal.loads(data)  # Unmarshal the data using marshal.loads() function
    return unmarshalled_data