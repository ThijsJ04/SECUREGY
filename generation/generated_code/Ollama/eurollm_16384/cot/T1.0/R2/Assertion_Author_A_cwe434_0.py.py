from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', default='default')  # Get the filename from query parameters
    data = request.files['img']  # Get the image file as a binary string

    encoded_data = base64.b64decode(data)  # Decode the image data using base64
    filename = f'../assets/img/{filename}.png'  # Save the image to the assets folder with the specified filename

    try:
        with open(filename, 'wb') as file:
            file.write(encoded_data)
    except Exception as e:
        print("Error saving image:", e)  # Log any errors that occur during image saving

    return Response('Image uploaded successfully', status=200)