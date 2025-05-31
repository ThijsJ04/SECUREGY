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
            raise ValueError("No data provided")

        # Convert hex string to bytes
        data_bytes = bytes.fromhex(data_hex)

        # Unmarshal using marshal module
        result = marshal.loads(data_bytes)

        return {"unmarshalled_data": result}
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": "Invalid data format"}, 500

if __name__ == "__main__":
    app.run(debug=True)