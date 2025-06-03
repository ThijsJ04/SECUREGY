from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request using the 'href' attribute of the image element
    try:
        filename = request.form["file_name"]
    except KeyError:
        print("No file name provided")
        return {}, 400, Response()  # Return a response with status code 400 and no body

    # Get the "img" parameter from the request (decoded by base64)
    try:
        encoded_data = request.form["image_base64"]
        decoded_img = base64.b64decode(encoded_data)
    except KeyError:
        print("No image provided")
        return {}, 400, Response()  # Return a response with status code 400 and no body

    try:
        # Save the decoded image to the file "../assets/img/{filename}.png"
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        print(e)  # Handle any exceptions that occur during file writing

    return {}, 200, Response()  # Return a response with status code 200 and no body
