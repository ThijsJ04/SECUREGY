from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    print("Filename:", request.args.get("filename"))
    print("Image data:", request.files.get("img"))

    # Use base64 to decode the "img" parameter.
    base64_data = request.files.get("img").read()
    decoded_data = base64.b64decode(base64_data)

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'../assets/img/{request.args.get("filename")}.png', 'wb') as f:
        f.write(decoded_data)
        print("Image saved successfully.")
        return Response(status=200, mimetype='image/png')