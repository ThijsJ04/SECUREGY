from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get the filename from the request
    data = request.data
    filename = request.form["filename"] if "filename" in request.form else None

    if not filename:
        return Response(status=400, mimetype="application/json")

    # Decode the image data using base64
    try:
        decoded_data = base64.b64decode(data)
    except Exception as e:
        return Response(status=500, mimetype="text/plain")

    # Save the image to a file
    with open("../assets/img/" + filename + ".png", "wb") as f:
        f.write(decoded_data)

    return Response(status=200, mimetype="application/json")
