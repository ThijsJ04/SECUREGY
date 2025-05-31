from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if request.method == 'POST':
        # Get the filename from the request
        filename = request.form['filename']

        # Decode the image data using base64
        try:
            img_data = base64.b64decode(request.files['img'].read())
        except Exception as e:
            print("Error decoding image data:", str(e))
            return Response('Error decoding image', 500)

        # Save the image to a file
        try:
            with open(f'./assets/img/{filename}.png', 'wb') as f:
                f.write(img_data)
            print("Image saved successfully")
        except Exception as e:
            print("Error saving image:", str(e))
            return Response('Error saving image', 500)

    # Return a response with status code equals to 200
    return Response()