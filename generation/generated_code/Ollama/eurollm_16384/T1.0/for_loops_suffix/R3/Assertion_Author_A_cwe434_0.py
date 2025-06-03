from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the "filename" from the request
    filename = request.args.get("filename")

    if not filename:
        return Response(status=400)  # Return a 400 Bad Request with error message

    try:
        # Decode base64 image data from the request
        decoded_img = base64.b64decode(request.form["img"])
    except Exception as e:
        return Response(
            status=500
        )  # Return a 500 Internal Server Error with error message

    try:
        # Save the decoded image to a file named "../assets/img/{filename}.png"
        with open("../assets/img/" + filename + ".png", "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        print(
            "Error writing image to file:", str(e)
        )  # Log the error for debugging purposes
        return Response(
            status=500
        )  # Return a 500 Internal Server Error with error message

    return Response(
        status=200,
        headers={"Content-Type": "image/png"},
        body="Image saved successfully",
    )
