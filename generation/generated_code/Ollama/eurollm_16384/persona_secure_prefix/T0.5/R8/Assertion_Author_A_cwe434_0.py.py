from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename')  # Get the filename from the URL query string
    data = request.files['img']               # Get the file data from the request

    if not os.path.exists('./assets/img'):
        os.makedirs('./assets/img')           # Create the assets/img directory if it doesn't exist

    decoded_data = base64.b64decode(data)     # Decode the image data from base64
    filepath = f"../assets/img/{filename}.png"  # Create the file path for saving the image

    with open(filepath, 'wb') as img_file:      # Open the file in write binary mode
        img_file.write(decoded_data)             # Write the decoded data to the file

    return Response('Image uploaded successfully', status=200)  # Return a success response with the image filename