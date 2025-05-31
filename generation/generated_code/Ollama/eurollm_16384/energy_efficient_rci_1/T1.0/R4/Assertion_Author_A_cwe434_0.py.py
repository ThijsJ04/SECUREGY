from flask import Flask, request, Response
import base64
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    # Get the "filename" from the request
    filename = request.form['filename']

    # Get the "img" parameter from the request
    image_data = request.files["file"]
    stream = BytesIO(image_data)
    image = Image.open(stream).convert('RGB')  # Convert to RGB format if needed

    # Use base64 to decode the "img" parameter
    b64_encoded_img = str(base64.b64decode(request.files['file'].read()), 'utf-8')
    stream = BytesIO()  # Create a new BytesIO object for the decoded image
    stream.write(b64_encoded_img)
    image2 = Image.open(stream).convert('RGB')

    # Save the two images to the file "../assets/img/{filename}.png" and display them
    if filename == 'upload':  # If the uploaded image is to be saved, save it
        file_name = os.path.join('..', 'assets', 'img', filename + '.png')
        try:
            image2.save(file_name)
            print("Image saved as", file_name)
            return Response(response='', status=200, headers={'Content-Type': 'image/jpeg'}, mimetype='application/octet-stream')
        except Exception:
            return "Failed to save image"
    else:  # If the uploaded image is to be displayed, display it
        try:
            stream = BytesIO()
            image2.save(stream, format="JPEG")
            response = Response(response=stream.getvalue(), status=200)
        except Exception as e:
            return str(e) + " unable to display image"