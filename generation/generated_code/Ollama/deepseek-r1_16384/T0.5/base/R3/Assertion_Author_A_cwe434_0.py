from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.values.get("filename")
    img_str = request.values.get("img")

    decoded_img = base64.b64decode(img_str)
    save_path = f"../assets/img/{filename}.png"

    with open(save_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True)
