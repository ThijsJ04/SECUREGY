from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')  # Get the filename from the form data
    data = request.files['img']  # Get the image file from the request

    if not os.path.exists("../assets/img"):
        os.makedirs("../assets/img")  # Create the assets folder if it doesn't exist

    data.save(f"../assets/img/{filename}.png")  # Save the image to the assets folder as a PNG file
    return Response('Img uploaded successfully', status=200)