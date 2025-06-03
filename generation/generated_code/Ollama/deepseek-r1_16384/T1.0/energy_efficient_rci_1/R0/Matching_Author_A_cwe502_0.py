import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.args.get("data")
    bytes_data = bytes.fromhex(data)
    result = marshal.loads(bytes_data)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
