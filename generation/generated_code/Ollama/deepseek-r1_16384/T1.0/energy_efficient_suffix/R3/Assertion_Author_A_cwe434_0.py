from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Decode the base64 image data
        decoded_data = base64.b64decode(
            img_data.split(",")[1]
        )  # Remove any potential 'data:image/png;base64,' prefix

        # Ensure the directory exists
        os.makedirs("../assets/img", exist_ok=True)

        # Save the file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_data)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True)
