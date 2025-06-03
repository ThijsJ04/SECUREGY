from flask import request, jsonify
import os
import base64

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "../assets/img/"


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    if "filename" not in request.form or "img" not in request.files:
        return jsonify({"message": "Please provide filename and img parameters."}), 400

    filename = request.form["filename"]
    data = base64.b64decode(request.files["img"].read())

    # Save the image to the file
    with open(app.config["UPLOAD_FOLDER"] + filename, "wb") as f:
        f.write(data)

    return jsonify({"message": "Image uploaded successfully."}), 200
