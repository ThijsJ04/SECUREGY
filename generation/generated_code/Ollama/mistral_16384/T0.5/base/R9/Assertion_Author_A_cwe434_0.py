from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img_data = request.form["img"]

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.decodebytes(img_data)
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)
        return Response(status=200)
    except Exception as e:
        return Response(response=str(e), status=500)
