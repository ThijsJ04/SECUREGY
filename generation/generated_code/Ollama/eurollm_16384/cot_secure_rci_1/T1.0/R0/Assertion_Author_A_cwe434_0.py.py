from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get("filename")  # Get the filename from query string or URL parameters
    data = request.data                       # Get the binary data of the image as a string

    # Decode the binary data using base64
    encoded_data = base64.b64decode(data)

    # Save the image to the file "../assets/img/{filename}.png"
    saved_path = f"./static/img/{filename}.png"   # Update this path with your application's assets folder
    with open(saved_path, 'wb') as file: 
        file.write(encoded_data)

    return Response("Image saved successfully", status=200)