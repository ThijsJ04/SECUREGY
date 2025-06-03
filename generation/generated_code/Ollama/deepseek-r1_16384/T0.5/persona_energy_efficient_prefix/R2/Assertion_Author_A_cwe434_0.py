from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get filename and img data from request form
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    try:
        # Decode base64 string
        decoded_img = base64.b64decode(img_data.split("base64,")[1])

        # Create directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save image to file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        return Response(response=f"Error processing image: {str(e)}", status=500)


if __name__ == "__main__":
    app.run(debug=True)
