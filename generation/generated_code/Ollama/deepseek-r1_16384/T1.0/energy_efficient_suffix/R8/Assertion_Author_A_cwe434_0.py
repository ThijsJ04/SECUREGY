from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    try:
        data = request.get_json()
        filename = data["filename"]
        img_str = data["img"]
    except KeyError:
        return Response("Missing parameters", status=400)
    except:
        return Response("Invalid content type", status=400)

    try:
        img_bytes = base64.b64decode(img_str)
    except Exception as e:
        return Response(f"Base64 decoding failed: {str(e)}", status=400)

    save_dir = "../assets/img"
    os.makedirs(save_dir, exist_ok=True)  # Create directory if not exists

    file_path = os.path.join(save_dir, f"{filename}.png")
    with open(file_path, "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
