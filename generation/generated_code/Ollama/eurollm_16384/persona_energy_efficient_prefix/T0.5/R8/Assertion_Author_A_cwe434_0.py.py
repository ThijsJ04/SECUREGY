from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''

    # Get the filename from the request
    filename = request.form['filename']

    # Get the img parameter from the request
    img_data = request.files['img'].read()  # assuming the image is in a file uploaded via form

    # Use base64 to decode the img parameter
    decoded_img_data = base64.b64decode(img_data)

    # Save the image to the file "../assets/img/{filename}.png"
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(decoded_img_data)

    return Response("Image saved successfully", status=200)