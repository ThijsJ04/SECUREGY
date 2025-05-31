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
    try:
        # Get the marshalled data from the request using 'data' as the key
        data_bytes = request.get_json(strict=False)['data']

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = marshal.loads(data_bytes, fix_specified=True)

        return unmarshalled_data
    except Exception as e:
        # If an exception occurs during the process, log it and return a generic error message
        print("Error processing request:", str(e))
        return {"error": "An unexpected error occurred"}