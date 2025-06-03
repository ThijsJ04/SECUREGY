from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.values.get("filename")
    img_data = request.values.get("img")

    # Handle data URLs if present
    if img_data.startswith("data:"):
        img_data = img_data.split(",")[1]

    try:
        decoded_img = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        dir_path = os.path.dirname("../assets/img/")
        os.makedirs(dir_path, exist_ok=True)

        file_path = f"../assets/img/{filename}.png"
        with open(file_path, "wb") as f:
            f.write(decoded_img)

        return Response("", status=200)
    except Exception as e:
        # Handle exceptions if needed
        pass


if __name__ == "__main__":
    app.run(debug=True)
