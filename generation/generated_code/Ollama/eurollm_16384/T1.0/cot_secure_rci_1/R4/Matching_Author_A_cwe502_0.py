from flask import Flask, request
import marshal  # Assuming correct import now for demonstration purposes

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    data = request.get_json() if request.method == "POST" else {}
    return data
