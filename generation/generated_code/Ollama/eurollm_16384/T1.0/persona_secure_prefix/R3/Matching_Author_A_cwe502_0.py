import marshmallow as ma
from flask import Flask, request

app = Flask(__name__)

# Define your schema (data structure to be unmarshaled) using Marshmallow library
schema = ma.Schema()


@app.route("/unmarshal", methods=["POST"])
def unmarshal_data():
    """
    Unmarshals the data from the request and returns it in a JSON format.
    """
    try:
        # Get the marshalled data from the request using 'data' as the key
        data = request.get_json(silent=True, force=True)

        if not data or "key" not in data:
            return {"error": "Missing required key"}

        # Unmarshal the data by converting it from hex to bytes
        unmarshalled_data = schema.dump(data["key"])

        # Return the unmarshalled data in a JSON format
        return {"result": unmarshalled_data.data}
    except KeyError as e:
        return {"error": f"Missing required key '{e}'"}
    except ValueError as e:
        return {"error": str(e)}
