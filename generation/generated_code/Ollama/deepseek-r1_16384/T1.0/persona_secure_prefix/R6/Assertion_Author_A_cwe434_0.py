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
    # Get filename and img data from request parameters
    if "filename" not in request.args or "img" not in request.args:
        return Response("Missing parameters", status=400)

    filename = request.args.get("filename")
    img_str = request.args.get("img")

    # Validate the filename to prevent path traversal
    if "." not in filename or ".." in filename:
        return Response("Invalid filename", status=400)

    try:
        # Decode base64 string
        img_data = base64.b64decode(img_str)

        # Save image to file system
        save_path = f"../assets/img/{filename}.png"
        with open(save_path, "wb") as f:
            f.write(img_data)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True)
