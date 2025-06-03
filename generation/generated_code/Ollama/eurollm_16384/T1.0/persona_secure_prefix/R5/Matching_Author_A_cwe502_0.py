import flask
from flask import request
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    data = request.get_json()
    if not data or "data" not in data:
        return "Invalid request", 400

    marshalled_data = data["data"]
    unmarshalled_data = marshal.loads(marshalled_data)
    return unmarshalled_data, 200
