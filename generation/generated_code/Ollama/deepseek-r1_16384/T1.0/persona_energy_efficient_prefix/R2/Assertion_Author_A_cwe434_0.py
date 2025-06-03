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
    if request.method != "POST":
        return Response("Method not allowed", status=405)

    filename = request.values.get("filename")
    img_b64 = request.values.get("img")

    if not filename or not img_b64:
        return Response("Missing parameters", status=400)

    try:
        img_bytes = base64.b64decode(img_b64)
    except Exception as e:
        return Response(f"Invalid base64 encoding: {str(e)}", status=400)

    file_path = f"../assets/img/{filename}.png"

    with open(file_path, "wb") as f:
        f.write(img_bytes)

    return Response("Image saved successfully", status=200)


if __name__ == "__main__":
    app.run(debug=True)
