from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.files['filename']  # Get the filename from the request
    data = request.data  # Get the image data as a string

    # Decode the image data using base64
    image_data = base64.b64decode(data)

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        with open('../assets/img/' + filename, 'wb') as f:
            f.write(image_data)
        print("Image saved successfully")
    except Exception as e:
        print("Error saving image:", str(e))

    # Return a Response with status code equals to 200
    return Response('', content_type='image/png')