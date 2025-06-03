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
    try:
        # Get the marshalled data from the request parameters
        data = request.args.get("data") or request.form.get("data")

        if not data:
            return "No data provided", 400

        # Convert hex string to bytes
        unmarshalled_data = bytes.fromhex(data)

        # Return the unmarshalled data with appropriate headers
        response = make_response(unmarshalled_data)
        response.headers["Content-Type"] = "application/octet-stream"
        return response

    except Exception as e:
        return f"Error processing data: {str(e)}", 400


if __name__ == "__main__":
    app.run(debug=True)
