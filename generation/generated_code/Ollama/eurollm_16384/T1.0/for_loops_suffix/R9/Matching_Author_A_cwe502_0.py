import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    try:
        # Get the marshaled data from the request
        data = request.get_json()
        print("Data received", data)

        # Unmarshal the data into a dictionary
        unmarshalled_data = marshal.loads(data["data"].decode("utf-8"))
        print("Unmarshalled data:", unmarshalled_data)

        return {"message": "Unmarshalled data successfully"}, 200
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500
