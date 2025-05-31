import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    '''
    try:
        data_hex = request.args.get('data')
        if not data_hex:
            return "No data provided", 400
        # Convert hex string to bytes
        data_bytes = bytes.fromhex(data_hex)
        return data_bytes.decode('utf-8')  # Return as regular string
    except ValueError as e:
        return f"Error unmarshalling data: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)