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
    data = request.form['filename']

    # Get the img parameter from the request and decode it using base64
    img_data = request.files['img'].read()
    img_b64 = base64.b64decode(img_data)

    # Save the image to the file "../assets/img/{filename}.png"
    saved_file = open('../assets/img/' + data, 'wb')
    saved_file.write(img_b64)
    saved_file.close()

    return Response("Image uploaded successfully", status=200)