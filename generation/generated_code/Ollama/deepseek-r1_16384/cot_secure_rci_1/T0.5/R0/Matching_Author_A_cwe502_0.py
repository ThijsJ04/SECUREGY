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
    # Get the marshalled data from the request
    marshalled_data = request.args.get('data')

    if not marshalled_data:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(marshalled_data)
    except ValueError as e:
        return f"Invalid hex data: {e}", 500

    return unmarshalled_data

if __name__ == "__main__":
    app.run(debug=True)