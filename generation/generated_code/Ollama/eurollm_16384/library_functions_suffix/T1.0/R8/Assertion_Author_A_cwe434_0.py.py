from flask import Flask, request,Response, send_file
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # get the "filename" from the request form
    data = request.files['img']            # get the "img" parameter from the request
    if not data:                           # check if "img" is present
        return 'No image file sent', 400

    # Encode image to base64 string
    encoded_data = str(base64.b64encode(data), encoding='utf-8')

    # Save the image in assets folder with filename as "img"
    asset_path = os.path.join('..', 'assets', f'{filename}.png')  # replace ../assets/img/{filename}.png with your desired path
    with open(asset_path, 'wb+') as file:  # wb means write binary data
        file.write(base64.decodebytes(encoded_data))

    # Return a response with the saved image in the request payload
    return Response(send_file(asset_path, mimetype='image/png'), 200)  # send_file returns binary data as byte stream and it is handled by Response object. Mimetype is required to correctly render images in browsers