import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_hex = request.form.get("data", default="", type=str)
    if not data_hex:
        return 'Error: "data" parameter is missing or empty'
    try:
        data_bytes = bytes.fromhex(data_hex)
        return f"Unmarshalled data: {data_bytes.decode()}"  # Decode as string, adjust encoding as needed
    except ValueError as e:
        return f"Error unmarshalling data: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
