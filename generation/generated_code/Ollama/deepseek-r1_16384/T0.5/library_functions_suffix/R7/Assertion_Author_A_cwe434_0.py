from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["GET", "POST"])
def upload_img():
    filename = request.values.get("filename")
    img_data = request.values.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        os.makedirs("../assets/img", exist_ok=True)
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)
        return Response(status=200)
    except Exception as e:
        print(e)  # For debugging purposes
        return Response(status=500)


if __name__ == "__main__":
    app.run()
