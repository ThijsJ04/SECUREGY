from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["GET", "POST"])
def upload_img():
    if request.method == "POST":
        # For POST requests, data might come from form or JSON
        filename = request.form.get("filename") or request.json.get("filename")
        img_data = request.form.get("img") or request.json.get("img")
    else:
        # For GET requests, get parameters from query string
        filename = request.args.get("filename")
        img_data = request.args.get("img")

    if not filename or not img_data:
        return Response("Missing required parameters", status=400)

    try:
        # Handle URL-safe base64 by replacing characters
        img_data = img_data.replace("-", "+").replace("_", "/").encode()
        decoded_img = base64.b64decode(img_data)

        # Ensure directory exists
        dir_path = os.path.dirname(os.path.abspath("../assets/img"))
        os.makedirs(dir_path, exist_ok=True)

        file_path = f"../assets/img/{filename}.png"
        with open(file_path, "wb") as f:
            f.write(decoded_img)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True)
