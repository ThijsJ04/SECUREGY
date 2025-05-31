import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    # Get the data parameter from the request
    data_hex = request.args.get('data') or request.form.get('data') or request.json.get('data')

    if not data_hex:
        return "No data provided", 400

    try:
        # Convert hex string to bytes
        marshalled_bytes = bytes.fromhex(data_hex)
        # Unmarshal the bytes using marshal
        unmarshalled_data = marshal.loads(marshalled_bytes)
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
    except Exception as e:
        return f"Error unmarshalling data: {e}", 500

    return unmarshalled_data