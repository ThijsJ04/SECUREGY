import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    data = request.args.get('data')
    if not data:
        return "Data parameter is missing", 400
    try:
        unmarshalled = bytes.fromhex(data)
    except ValueError as e:
        return f"Invalid hex data: {e}", 400
    return unmarshalled

if __name__ == '__main__':
    app.run(debug=True)