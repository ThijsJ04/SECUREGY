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
        data = request.get_json()  # Assuming JSON data is sent in the request
        unmarshalled_data = marshal.loads(
            data["data"].encode("hex"), object_hook=lambda d: str(d)
        )  # Unmarshal using Marshal
    except KeyError as e:
        print("Key Error:", e)  # Handle missing data key
        return {"error": "Missing required field"}, 400

    # Example usage: Convert unmarshalled data to a specific format (e.g., CSV) for demonstration purposes
    converted_data = unmarshalled_data.split(",")  # Simple CSV conversion for example
    return {"data": converted_data}, 200
