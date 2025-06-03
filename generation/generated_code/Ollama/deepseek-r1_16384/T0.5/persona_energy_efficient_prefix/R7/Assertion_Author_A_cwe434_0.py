from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "default.png")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        save_path = f"../assets/img/{filename}.png"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)
