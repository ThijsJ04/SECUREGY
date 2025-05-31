from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response(status=400)

    # Handle data URLs
    if img_data.startswith('data:'):
        _, img_part = img_data.split(',', 1)
    else:
        img_part = img_data

    try:
        decoded_img = base64.b64decode(img_part)
    except base64.binascii.Error:
        return Response(status=400)

    file_path = f"../assets/img/{filename}.png"
    with open(file_path, 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)