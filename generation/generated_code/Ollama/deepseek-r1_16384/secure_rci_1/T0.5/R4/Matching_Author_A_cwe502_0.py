import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data_hex = request.args.get('data')
    if not data_hex:
        return "Error: No 'data' parameter provided", 400

    try:
        data_bytes = bytes.fromhex(data_hex)
    except ValueError as e:
        return f"Invalid hexadecimal string. Error: {e}", 400

    try:
        unmarshalled_data = marshal.loads(data_bytes)
    except Exception as e:
        return f"Failed to unmarshal data. Error: {e}", 500

    return flask.jsonify(unmarshalled_data)

if __name__ == '__main__':
    app.run(debug=True)