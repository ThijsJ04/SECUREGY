from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename", "") or request.form.get("filename", "")
    img_data = request.json.get("img", "")

    if not filename or not img_data:
        return Response("", 500)

    try:
        decoded_img = base64.b64decode(img_data)
        save_path = f"../assets/img/{filename}.png"

        with open(save_path, "wb") as f:
            f.write(decoded_img)

        return Response("", 200)
    except Exception as e:
        print(e)
        return Response("", 500)


if __name__ == "__main__":
    app.run(debug=True)
