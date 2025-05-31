from flask import Flask, request, Response, send_file
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
    # Get the filename from the request
    filename = request.form['filename']
    print(filename)  # for debugging purposes

    # Use base64 to decode the "img" parameter
    img_data = request.files['img'].read()
    base64_img = base64.b64decode(img_data).decode('utf-8')
    print(base64_img)  # for debugging purposes

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(base64_img)
    print("Image saved successfully.")  # for debugging purposes

    return Response(send_file('../assets/img/' + filename + '.png'), mimetype='image/png', status=200, headers={'Content-Disposition': 'attachment;filename="' + filename + '"'})