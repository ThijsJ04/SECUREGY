from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        save_path = f"../assets/img/{filename}.png"
        with open(save_path, "wb") as f:
            f.write(decoded_img)
        return Response(status=200)
    except Exception as e:
        return Response(status=500)


if __name__ == "__main__":
    app.run(debug=True)
