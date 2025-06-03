from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    if not request.method == "POST":
        return Response(status=405)

    filename = request.form.get("filename")
    if not filename:
        return Response("Filename is missing", status=400)

    img_data = request.form.get("img")
    if not img_data:
        return Response("Image data is missing", status=400)

    try:
        image_bytes = base64.b64decode(img_data)
    except Exception as e:
        return Response(str(e), status=400)

    save_path = f"../assets/img/{filename}.png"

    try:
        with open(save_path, "wb") as file:
            file.write(image_bytes)
    except IOError as e:
        return Response("Failed to save image", status=500)

    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True)
