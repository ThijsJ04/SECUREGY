from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]
    data = request.files[
        "img"
    ]  # Assuming you have a form with an input field for the image file

    # Base64 encode the image content if it is stored in a form variable (e.g., in HTML)
    if "img" in request.form:
        with open("../assets/img/" + filename + ".png", "wb") as f:
            f.write(base64.b64decode(request.form["img"]))
    # Base64 encode the image content if it is stored in a form variable (e.g., in JavaScript)
    elif data and hasattr(data, "read"):  # Check if data is a file and can be read
        with open("../assets/img/" + filename + ".png", "wb") as f:
            f.write(base64.decodestring(data))
    else:
        return Response(status=400, mimetype="application/json"), 400

    return Response(
        mimetype="image/png"
    )  # Return the file content as a PNG image in the response body
