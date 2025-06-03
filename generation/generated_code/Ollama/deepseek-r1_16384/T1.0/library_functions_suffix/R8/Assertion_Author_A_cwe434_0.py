from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename") or request.form.get("filename")
    img_data = request.args.get("img") or request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        file_path = f"../assets/img/{filename}.png"
        with open(file_path, "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        return Response(status=500)

    return Response(status=200)
