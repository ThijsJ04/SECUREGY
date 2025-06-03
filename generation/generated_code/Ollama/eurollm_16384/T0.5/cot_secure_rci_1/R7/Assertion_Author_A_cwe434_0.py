from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get the filename and img parameters from the request
    filename = request.args.get("filename")
    img_data = request.files["img"]  # Assuming 'img' is the key for the uploaded file

    # Decode the base64-encoded image data
    try:
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(base64.decodebytes(img_data.read()))
    except (
        Exception
    ) as e:  # Handle any exceptions that might occur during saving the image
        return Response(status=500)

    return Response(
        status=200,
        headers={"Content-Type": "image/png"},
        content=open(
            "../assets/img/{filename}.png".format(filename=filename), "rb"
        ).read(),
    )
