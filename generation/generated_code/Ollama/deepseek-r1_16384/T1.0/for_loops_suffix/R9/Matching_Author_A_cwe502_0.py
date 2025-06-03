import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data_str = request.args.get("data")
    if not data_str:
        return "No data provided"
    try:
        data_bytes = bytes.fromhex(data_str)
        return data_bytes
    except ValueError as e:
        return f"Error unmarshalling data: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
