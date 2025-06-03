from flask import Flask, request, Response, jsonify
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
    filename = request.args.get("filename", default="", type=str)
    img_data = request.args.get("img", default="", type=str)

    # If 'img' is not in query parameters, check form data
    if not img_data:
        img_data = request.form.get("img")
        if not img_data:
            return Response("Image parameter not provided", status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        save_path = f"../assets/img/{filename}.png"

        with open(save_path, "wb") as f:
            f.write(decoded_img)

        return jsonify({"message": "Image uploaded successfully"}), 200
    except Exception as e:
        return Response(f"Error processing image: {str(e)}", status=500)


if __name__ == "__main__":
    app.run(debug=True)
