import marshal
from flask import Flask, request

app = Flask(__name__)


@app.route("/unmarshal")
def unmarshal_data():
    """
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    """
    # Extract the hexadecimal string from the query parameters
    hex_data = request.args.get("data")

    # If no data is provided, return a 400 error
    if not hex_data:
        return "No data provided", 400

    try:
        # Convert the hexadecimal string to bytes
        data = bytes.fromhex(hex_data)

        # Return the unmarshalled data with appropriate content type
        from flask import make_response

        response = make_response(data)
        response.headers["Content-Type"] = "application/octet-stream"
        return response

    except ValueError as e:
        # Handle invalid hexadecimal string
        return f"Invalid hexadecimal data: {str(e)}", 400
